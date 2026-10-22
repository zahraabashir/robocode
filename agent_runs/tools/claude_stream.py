"""Normalize saved Claude stream records without executing commands or prompts.

Tool requests are paired to responses by session and tool-use ID, never by
proximity. Helper identity is retained. Empty thinking and routine progress stay
in the raw stream and coverage ledger rather than becoming decision events.
"""
import collections
import json


def text_content(value):
    if isinstance(value,str):return value
    if isinstance(value,list):
        return '\n'.join(b.get('text','') if b.get('type')=='text' else json.dumps(b,ensure_ascii=False) for b in value)
    return json.dumps(value,ensure_ascii=False)


def normalize_claude(raw, tagger, summarizer):
    rows=[json.loads(line) for line in raw.splitlines()]
    calls={};resolved=set();events=[];covered=[];ignored=[];thinking=collections.Counter()
    session=0; sessions={}
    def contents(obj):
        value=obj.get('message',{}).get('content',[])
        return value if isinstance(value,list) else [{'type':'text','text':value}]
    for line,obj in enumerate(rows,1):
        if obj.get('type')=='system' and obj.get('subtype')=='init':session+=1
        sessions[line]=session
        for index,b in enumerate(contents(obj),1):
            if b.get('type')=='tool_use':
                key=(obj.get('session_id'),b['id'])
                if key in calls:raise ValueError(f'Duplicate tool request at line {line}; review replay semantics')
                calls[key]=(line,index,b,obj)
    def add(line,index,obj,item,kind='completed_item',start=None,request=None):
        blocks=contents(obj)
        eid=f'E{line:04d}'+(f'B{index:02d}' if index and len(blocks)>1 else '')
        parent=obj.get('parent_tool_use_id')
        actor=('helper: '+str(obj.get('task_description') or parent)) if parent else 'main stream'
        events.append(dict(id=eid,source_line=line,source_block=index,turn=sessions[line],start_line=start,
            kind=kind,tags=tagger(item),summary=summarizer(item),item=item,
            parent_tool_use_id=parent,actor=actor,session_id=obj.get('session_id'),
            timestamp=obj.get('timestamp'),source_payload=blocks[index-1] if index else obj,
            request_payload=request))
        covered.append({'line':line,'block':index,'event':eid,'role':'result_or_message'})
    for line,obj in enumerate(rows,1):
        typ=obj.get('type');sub=obj.get('subtype')
        if typ in ('assistant','user'):
            for index,b in enumerate(contents(obj),1):
                bt=b.get('type')
                if bt=='tool_use':continue
                if bt=='thinking':
                    thinking['records']+=1
                    if not b.get('thinking'):
                        thinking['empty_readable_text']+=1
                        ignored.append({'line':line,'block':index,'reason':'empty thinking text; signature is not readable reasoning'})
                        continue
                    thinking['nonempty_readable_text']+=1
                    add(line,index,obj,dict(type='readable_thinking',text=b['thinking']))
                elif bt=='text':
                    add(line,index,obj,dict(type='agent_message' if typ=='assistant' else 'saved_context_message',text=b.get('text','')))
                elif bt=='tool_result':
                    key=(obj.get('session_id'),b.get('tool_use_id'));request=calls.get(key)
                    if key in resolved:raise ValueError(f'Duplicate tool result at {line}; review replay semantics')
                    resolved.add(key)
                    start,reqindex,call,callobj=request if request else (None,None,{}, {})
                    name=call.get('name','unknown');args=call.get('input',{});output=text_content(b.get('content',''))
                    meta=obj.get('tool_use_result',{})
                    if not isinstance(meta,dict):meta={'saved_value':meta}
                    common=dict(id=b.get('tool_use_id'),tool_name=name,tool_input=args,
                        aggregated_output=output,tool_result_is_error=b.get('is_error'),
                        result_metadata=meta,status='tool_returned',
                        background_launch=bool(meta.get('backgroundTaskId') or meta.get('isAsync') or 'running in background' in output.lower()))
                    if name=='Bash':item=dict(type='command_execution',command=args.get('command',''),exit_code=meta.get('exitCode',meta.get('exit_code')),**common)
                    elif name in ('Write','Edit','MultiEdit'):
                        path=args.get('file_path',args.get('path',''))
                        item=dict(type='file_change',changes=[{'path':path,'kind':name.lower()}],**common)
                    elif name in ('Agent','Task','SendMessage'):
                        item=dict(type='collab_tool_call',tool=name,prompt=args.get('prompt',args.get('message','')),**common)
                    else:item=dict(type='mcp_tool_call',tool=name,arguments=args,**common)
                    add(line,index,obj,item,start=start,request=call or None)
                    if request:covered.append({'line':start,'block':reqindex,'event':events[-1]['id'],'role':'tool_request'})
                else:
                    add(line,index,obj,dict(type='unrecognized_content',data=b),kind='unrecognized')
        elif typ=='tool_progress' or (typ=='system' and sub in ('task_progress','background_tasks_changed','task_updated')):
            ignored.append({'line':line,'block':None,'reason':'routine progress metadata; retained in raw stream'})
        else:
            # Preserve task notifications (including helper conclusions), context
            # compaction, effort changes, session initialization and final result.
            if typ=='result':item=dict(type='run_result',text=obj.get('result',''),data=obj)
            elif typ=='system':item=dict(type='system_record',subtype=sub,text=obj.get('summary',obj.get('description','')),data=obj)
            else:item=dict(type='unrecognized_record',data=obj)
            add(line,None,obj,item,kind='boundary' if typ in ('result','system') else 'unrecognized')
    for key,(line,index,call,obj) in calls.items():
        if key not in resolved:
            add(line,index,obj,dict(type='unreturned_tool_request',tool=call.get('name'),arguments=call.get('input'),data=call),kind='unfinished_item',start=line)
    events.sort(key=lambda e:(e['source_line'],e.get('source_block') or 0))
    # Exact coverage of every message content block or top-level metadata record.
    expected={(i,j) for i,o in enumerate(rows,1) for j in (range(1,len(contents(o))+1) if o.get('type') in ('assistant','user') else [None])}
    observed=[(x['line'],x['block']) for x in covered+ignored]
    if len(observed)!=len(set(observed)) or set(observed)!=expected:raise ValueError('Claude coverage mismatch')
    audit=dict(raw_lines=len(rows),coverage=covered,raw_only=ignored,thinking=dict(thinking),
        source_types=dict(collections.Counter(o.get('type') for o in rows)),tool_requests=len(calls),
        tool_results=sum(e['item'].get('tool_name') is not None for e in events),
        helper_events=sum(bool(e.get('parent_tool_use_id')) for e in events),
        main_events=sum(not e.get('parent_tool_use_id') for e in events),
        scope='Every source content block or metadata record accounted for. Empty thinking and routine progress are raw-only. Helper events retain parent identity; background tool return does not establish job completion.')
    return events,audit
