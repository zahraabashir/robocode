"""Build review documents from read-only archive records. Never execute saved code.

The registry and annotations are local, editable inputs. Existing findings are
human-owned. Generated reading documents are overwritten only if still identical
to their last generated hashes. Codex and Claude stream adapters are supported.
"""
from pathlib import Path
import argparse
import collections
import hashlib
import html
import json
import re
import shlex
import shutil
import subprocess
from claude_stream import normalize_claude

ROOT = Path(__file__).resolve().parents[1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def stream_records(raw):
    """Keep exact line positions, including non-JSON launcher messages."""
    rows=[]
    for line in raw.splitlines():
        try:
            obj=json.loads(line)
            if not isinstance(obj,dict):raise ValueError('Expected object')
        except (ValueError,TypeError):
            obj={'type':'non_json_record','text':line}
        rows.append(obj)
    return rows


def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')


def cell(s, limit=150):
    s = re.sub(r'\s+', ' ', str(s)).strip()
    if len(s) > limit:
        s = s[:limit-1] + '…'
    return (html.escape(s).replace('|', '&#124;').replace('`', '&#96;')
            .replace('[', '&#91;').replace(']', '&#93;'))


def fence(s, language='text'):
    longest = max([len(m.group()) for m in re.finditer(r'`+', s)] or [0])
    marker = '`' * max(3, longest+1)
    return f'{marker}{language}\n{s}\n{marker}\n'


def file_kind(path):
    name = Path(path).name.lower()
    if name == 'approach.py':
        return 'policy'
    if any(s in name for s in ('test', 'probe', 'trace', 'inspect', 'survey', 'scan', 'debug', 'validate')):
        return 'diagnostic/test'
    if name.endswith('.py') and name != 'env_client.py':
        return 'support code (role needs review)'
    return 'setup/other'


def tags(item):
    typ = item.get('type', '')
    if typ=='system_record':return ['System: '+str(item.get('subtype'))]
    if typ=='run_result':return ['Run result / handoff']
    if typ=='saved_context_message':return ['Saved context message (not assumed human)']
    if typ=='readable_thinking':return ['Readable thinking text (saved)']
    if typ == 'agent_message':
        return ['Message']
    if typ == 'file_change':
        return sorted({file_kind(c.get('path', ''))+' edit' for c in item.get('changes', [])}) or ['Edit']
    if typ == 'command_execution':
        cmd = item.get('command', '')
        result = ['Command']
        if re.search(r'\bgit\s+commit\b', cmd): result.append('commit attempt')
        if re.search(r'\b(?:python[\w.]*|pytest)\b', cmd) and re.search(r'(?:test_|probe_|trace_|validate_|make_env|env\.step|e\.step|\.get_action\()', cmd):
            result.append('test/probe candidate')
        if re.search(r'\b(?:sed|cat|rg|head|tail|ls|git\s+(?:show|diff|log))\b', cmd): result.append('inspection candidate')
        if re.search(r'(?:apply_patch|write_text\(|write_bytes\(|\btee\s|\bcat\s*>)', cmd): result.append('edit candidate')
        return result
    if typ == 'collab_tool_call': return ['Delegation/coordination']
    if typ == 'mcp_tool_call': return ['Tool: '+str(item.get('tool', 'unknown'))]
    return ['Other: '+typ]


def summarize(item):
    typ = item.get('type', '')
    if typ in ('agent_message','saved_context_message','readable_thinking','run_result','system_record'):
        return item.get('text') or str(item.get('subtype') or typ)
    if typ == 'file_change':
        return '; '.join(c.get('kind', '')+' '+c.get('path', '') for c in item.get('changes', []))
    if typ == 'command_execution':
        command=item.get('command', '')
        try:
            parts=shlex.split(command)
            inner=parts[-1] if len(parts)>2 and parts[1] in ('-lc','-c') else command
        except ValueError: inner=command
        descriptions=[]
        title=re.search(r'git\s+commit\b.*?-m\s+([\'\"])(.*?)\1',inner,re.S)
        if title:descriptions.append('Commit: '+title.group(2))
        scripts=re.findall(r'(?:python[\w.]*\s+)(?:-\w+\s+)*([\w./-]+\.py)([^\n;&|]*)',inner)
        for script,args in scripts:
            descriptions.append('Run '+Path(script).name+(' '+args.strip() if args.strip() else ''))
        if re.search(r'python[\w.]*\s+(?:-\w+\s+)*-\s*<<',inner):descriptions.append('Run inline Python script (inspect code/output)')
        if not descriptions:
            action_tags=tags(item)
            if 'edit candidate' in action_tags:descriptions.append('Write or patch files; inspect exact command')
            elif 'inspection candidate' in action_tags:descriptions.append('Inspect files, output or repository state')
            else:descriptions.append('Run shell command; inspect exact command')
        return '; '.join(descriptions)
    if typ == 'collab_tool_call': return str(item.get('tool', ''))+' '+str(item.get('prompt') or '')
    if typ == 'mcp_tool_call': return str(item.get('tool', ''))+' '+json.dumps(item.get('arguments', {}), ensure_ascii=False)
    return typ


def output_summary(item):
    if item.get('type')=='command_execution':
        output=item.get('aggregated_output','')
        reports=re.findall(r'(?im)^.*?\b(?:success|solved)\s*[:=]?\s*\d+\s*/\s*\d+[^\n]*',output)
        status=(f"Process exit {item.get('exit_code')}" if item.get('exit_code') is not None else 'Exit code not recorded')
        if item.get('tool_result_is_error'):status+='; tool error'
        if item.get('background_launch'):status+='; background job launched'
        if reports:status+='; '+ ' / '.join(reports[-3:])
        elif 'Traceback (most recent call last)' in output:status+='; recorded traceback'
        return status
    if item.get('type')=='file_change':return 'Edit recorded; outcome not inferred'
    return '—'


def normalize(raw):
    events, starts, completed, turn = [], {}, set(), 0
    for line, obj in enumerate(stream_records(raw), 1):
        typ = obj.get('type', '')
        if typ == 'turn.started': turn += 1
        if typ == 'item.started':
            starts[(turn, obj['item'].get('id'))] = (line, obj['item'])
            continue
        if typ == 'item.updated': continue
        if typ == 'item.completed':
            item = obj['item']; key = (turn, item.get('id'))
            completed.add(key)
            events.append(dict(id=f'E{line:04d}', source_line=line, turn=turn,
                start_line=starts.get(key, (None,))[0], kind='completed_item',
                tags=tags(item), summary=summarize(item), item=item))
        else:
            events.append(dict(id=f'E{line:04d}', source_line=line, turn=turn,
                start_line=None, kind='boundary' if typ in ('thread.started','turn.started','turn.completed') else 'unrecognized',
                tags=['Boundary: '+typ] if typ in ('thread.started','turn.started','turn.completed') else ['Unrecognized record; review required'],
                summary=typ, item=obj))
    for key, (line, item) in starts.items():
        if key not in completed:
            events.append(dict(id=f'E{line:04d}', source_line=line, turn=key[0], start_line=line,
                kind='unfinished_item', tags=['No completion saved']+tags(item), summary=summarize(item), item=item))
    return sorted(events, key=lambda e:e['source_line'])


def numbered_diff(diff):
    old = new = None
    out = [' OLD   NEW   CHANGE']
    for line in diff.splitlines():
        m = re.match(r'@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@', line)
        if m:
            old, new = map(int, m.groups()); out.append(line)
        elif line.startswith(('diff --git', '--- ', '+++ ')):
            old = new = None; out.append(line)
        elif old is not None and line.startswith('+'):
            out.append(f'       {new:5d} {line}'); new += 1
        elif old is not None and line.startswith('-'):
            out.append(f'{old:5d}        {line}'); old += 1
        elif old is not None and line.startswith(' '):
            out.append(f'{old:5d}  {new:5d} {line}'); old += 1; new += 1
        else: out.append(line)
    return '\n'.join(out)


def build(rec):
    if rec['backend'] not in ('codex','claude'):
        raise ValueError('Unsupported stream backend; inspect its schema before import.')
    source = Path(rec['path']); out = ROOT/rec['directory']; evdir = out/'evidence'
    evdir.mkdir(parents=True, exist_ok=True)
    oldmanifest = json.loads((evdir/'manifest.json').read_text()) if (evdir/'manifest.json').exists() else {}
    for name in ('01_timeline.md', '02_code_changes.md'):
        p = out/name
        if p.exists() and sha(p.read_bytes()) != oldmanifest.get('generated_documents', {}).get(name):
            raise ValueError(f'Preserving edited document {p}. Move your annotation into evidence/annotations.json or keep this edited document before rebuilding.')
    annotations = json.loads((evdir/'annotations.json').read_text())
    copied = []
    def copy(src, dst):
        src=Path(src); dst=Path(dst)
        dst.parent.mkdir(parents=True,exist_ok=True)
        data=src.read_bytes(); dst.write_bytes(data)
        copied.append(dict(source=str(src),copy=str(dst.relative_to(out)),sha256=sha(data)))
    for src, dst, expected in [('stream.jsonl','stream.jsonl','stream_sha256'),
                               ('.hydra/config.yaml','config.yaml','config_sha256'),
                               ('sandbox/approach.py','final/approach.py','policy_sha256')]:
        assert sha((source/src).read_bytes()) == rec[expected], (rec['sample_id'],src,'source changed')
        copy(source/src,evdir/dst)
    for src,dst in [('env_description.md','task.md'),('results.json','results.json'),
                    ('.hydra/overrides.yaml','overrides.yaml'),('sandbox/agent_log.txt','agent_log.txt'),
                    ('sandbox/AGENTS.md','historical_instructions.txt'),('sandbox/CLAUDE.md','historical_claude_instructions.txt')]:
        if (source/src).is_file(): copy(source/src,evdir/dst)
    for p in (source/'sandbox').glob('*.py'):
        if p.name!='approach.py' and not p.is_symlink(): copy(p,evdir/'final'/p.name)
    if source.name=='run':
        for name in ('provenance.json','manifest.sha256.json'):
            if (source.parent/name).is_file():copy(source.parent/name,evdir/('export_'+name))
    def git(*args):
        return subprocess.check_output(['git','--no-optional-locks','-C',str(source/'sandbox'),*args],stderr=subprocess.PIPE)
    assert git('rev-parse','HEAD').decode().strip()==rec['git_head']
    assert sha(git('show','HEAD:approach.py'))==rec['policy_sha256']
    # Bundles retain all saved refs, trees, helpers and historical instruction bytes
    # without placing an active .git or AGENTS.md inside the inspection folder.
    bundle=evdir/'history.bundle'
    if not bundle.exists(): git('bundle','create',str(bundle),'--all')
    raw=(evdir/'stream.jsonl').read_text()
    if rec['backend']=='claude':
        events,coverage=normalize_claude(raw,tags,summarize)
        dump(evdir/'stream_coverage.json',coverage)
    else:events=normalize(raw)
    completed=[e for e in events if e['kind']=='completed_item']
    eventmap={e['source_line']:e for e in events}
    commits=[]; history=git('log','--reverse','--topo-order','--format=%H%x09%P%x09%aI%x09%s','HEAD').decode().splitlines()
    for index,line in enumerate(history,1):
        commit,parents,date,title=line.split('\t',3); parents=parents.split(); cid=f'C{index:03d}'
        names=git('diff-tree','--root','--no-commit-id','--name-only','-r',commit).decode().splitlines()
        diff=git('show','--format=','--no-ext-diff','--no-textconv','--root',commit).decode(errors='replace')
        dp=evdir/'diffs'/f'{cid}_{commit[:7]}.diff'; dp.parent.mkdir(exist_ok=True);dp.write_text(diff)
        matches=[]
        for e in completed:
            it=e['item']; command=it.get('command',''); output=it.get('aggregated_output','')
            if re.search(r'\[[^\]\n]*\b'+re.escape(commit[:7])+r'\b[^\]\n]*\]',output):
                matches.append({'event':e['id'],'evidence':'commit hash in recorded output'})
            elif 'git commit' in command and title in command:
                matches.append({'event':e['id'],'evidence':'commit title in command; output may not confirm creation'})
        ann=annotations.get('commits',{}).get(commit,{})
        c=dict(id=cid,commit=commit,parents=parents,date=date,title=title,files=names,
               file_roles=sorted({file_kind(n) for n in names}),diff=str(dp.relative_to(out)),
               diff_sha256=sha(dp.read_bytes()),events=matches,annotation=ann)
        if 'approach.py' in names:
            try: code=git('show',f'{commit}:approach.py')
            except subprocess.CalledProcessError: code=None
            if code is not None:
                p=evdir/'versions'/f'{cid}_{commit[:7]}_approach.py';p.parent.mkdir(exist_ok=True);p.write_bytes(code)
                c.update(policy_sha256=sha(code),version=str(p.relative_to(out)))
                c['same_policy_as_earlier']=[v['id'] for v in commits if v.get('policy_sha256')==c['policy_sha256']]
        commits.append(c)
    dump(evdir/'events.json',events); dump(evdir/'commits.json',commits)
    by_event=collections.defaultdict(list)
    for c in commits:
        for m in c['events']:by_event[m['event']].append(c)
    name=f"{rec['environment_name']} · {rec['model']} · replicate {rec['replicate_seed']}"
    timeline=[f'# {name}: development timeline','',
        '[Environment overview](../../overview.md) · [Code changes](02_code_changes.md) · [Findings and your notes](03_findings.md)','',
        f"Review status: **{rec['review_status']}**. Start with the table, then open an event below for its exact message, command and output.",'',
        'Event IDs preserve raw stream positions: E0401 means source line 401. Gaps are normal; started/update records are retained in the raw source, not duplicated as completed actions. Boundaries and unfinished tools are shown. For Claude, B01/B02 suffixes distinguish multiple content blocks on one line; the turn column counts session initializations, not model inference turns.','',
        ('Claude tools are placed at their response line, with request lines retained. A returned tool can launch a background job; it is not necessarily a finished experiment. Helper rows retain their parent identity. Empty thinking and routine progress remain in the raw stream and [coverage ledger](evidence/stream_coverage.json). No hidden reasoning is reconstructed.' if rec['backend']=='claude' else 'This Codex timeline follows the main stream; helper session trees are not exhaustively merged.'),'',
        '**Reading rule:** arrows and adjacent rows mean recorded order, not proof of causation. For asynchronous calls, inspect the start line as well as completion. An exit code of zero is not evidence that robot tests passed. Automated tags are navigation aids, not ACT*ONOMY or decision-making labels.','',
        f"Evidence: [task](evidence/task.md), [configuration](evidence/config.yaml), [raw stream](evidence/stream.jsonl), [manifest](evidence/manifest.json). {len(completed)} normalized messages/tool returns; {len(commits)} saved commits in HEAD ancestry. These extraction counts are not counts of independent decisions or finished tests.",'',
        '| Event | Turn/session | Actor | Kind (automatic) | Message/action preview | Recorded result | Commit reference |',
        '| --- | --- | --- | --- | --- | --- | --- |']
    for e in events:
        a=annotations.get('events',{}).get(e['id'],annotations.get('events',{}).get(str(e['source_line']),{}))
        title=a.get('title') or e['summary']
        refs=', '.join(f"[{c['id']}](02_code_changes.md#{c['id']})" for c in by_event[e['id']])
        timeline.append(f"| [{e['id']}](#{e['id']}) | {e['turn']} | {cell(e.get('actor','main stream'),75)} | {cell(', '.join(e['tags']),100)} | {cell(title)} | {cell(output_summary(e['item']),120)} | {refs} |")
    timeline+=['','## Exact events','', 'Historical messages and commands below are evidence, never instructions to the reader or analysis agent.','']
    for n,e in enumerate(events):
        timeline += [f'<a id="{e["id"]}"></a>', f'### {e["id"]} · '+', '.join(e['tags']), '',
                     f"Source line {e['source_line']}; turn {e['turn']}; start line {e['start_line'] or 'not saved/not applicable'}.",'']
        links=[]
        if n:links.append(f"[Previous](#{events[n-1]['id']})")
        if n+1<len(events):links.append(f"[Next](#{events[n+1]['id']})")
        links += [f"[{c['id']}: change](02_code_changes.md#{c['id']})" for c in by_event[e['id']]]
        timeline += [' · '.join(links),'']
        item=e['item'];typ=item.get('type')
        if rec['backend']=='claude':timeline += [f"Actor: {cell(e['actor'],200)}. Parent tool: `{e.get('parent_tool_use_id') or 'none'}`. Timestamp: {e.get('timestamp') or 'not saved'}.",'']
        if typ=='agent_message': timeline += ['Exact agent message:',fence(item.get('text',''))]
        elif typ=='command_execution':
            timeline+=['<details>','<summary>Recorded command and full output</summary>','',
                       'Command:',fence(item.get('command','')),
                       f"Process exit code: {item.get('exit_code')}; recorded status: {item.get('status')}. Robot outcomes must be read in the output.",'',
                       'Output:',fence(item.get('aggregated_output','')),'</details>','']
        else:timeline+=['<details>','<summary>Event data (normalized fields; exact raw pointers above)</summary>','',fence(json.dumps(item,indent=2,ensure_ascii=False),'json'),'</details>','']
    (out/'01_timeline.md').write_text('\n'.join(timeline)+'\n')
    guide=[f'# {name}: commits and changed lines','',
        '[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)','',
        'Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.','',
        'Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.','',
        '| Commit | Original title | Files/roles | Linked events |', '| --- | --- | --- | --- | --- |']
    for c in commits:
        alias=f" / {c['annotation']['alias']}" if c['annotation'].get('alias') else ''
        refs=', '.join(f"[{m['event']}](01_timeline.md#{m['event']})" for m in c['events']) or 'No matched commit command/output'
        guide.append(f"| [{c['id']}{alias}](#{c['id']}) · `{c['commit'][:7]}` | {cell(c['title'],200)} | {cell(', '.join(c['files']),180)} | {refs} |")
    guide+=['','## Change details','']
    for c in commits:
        guide += [f'<a id="{c["id"]}"></a>']
        if c['annotation'].get('alias'): guide.append(f'<a id="{c["annotation"]["alias"]}"></a>')
        guide += [f"### {c['id']} · {c['title']}",'',f"Commit `{c['commit']}`; parents: {', '.join(c['parents']) or 'none (initial snapshot)'}. Recorded author date: {c['date']}.",'',
                  'File roles (automatic): '+', '.join(c['file_roles'])+'.','']
        for m in c['events']:guide += [f"- [{m['event']}](01_timeline.md#{m['event']}): {m['evidence']}."]
        ann=c['annotation']
        if ann:
            guide+=['', '**Prior analyst description (carried forward, not independently relabeled):** '+ann.get('description',''), '']
            for caveat in ann.get('caveats',[]):guide+=['- '+caveat]
            related=[f"[E{line:04d}](01_timeline.md#E{line:04d})" for line in ann.get('related_lines',[]) if line in eventmap]
            tests=[f"[E{line:04d}](01_timeline.md#E{line:04d})" for line in ann.get('post_edit_test_lines',[]) if line in eventmap]
            guide+=['','Prior mapped context: '+', '.join(related)+'.','', 'Prior mapped post-edit test reports: '+(', '.join(tests) or 'none mapped')+'. These are not isolated causal tests.','']
        if c.get('version'):
            guide += [f"[Controller after this commit]({c['version']}) · [Exact all-file diff]({c['diff']})",'']
            prev=next((p for p in reversed(commits[:commits.index(c)]) if p.get('version')),None)
            if prev:guide += [f"[Previous saved controller snapshot]({prev['version']}) — not the first-ever controller.",'']
            if c['same_policy_as_earlier']:guide+=['Identical complete controller bytes to earlier '+', '.join(f"[{p}](#{p})" for p in c['same_policy_as_earlier'])+'. Other files may differ.','']
            if c['policy_sha256']==rec['policy_sha256']:guide+=['This controller snapshot is byte-identical to the final saved controller.','']
        else:guide += [f"[Exact all-file diff]({c['diff']})",'']
        guide+=['<details>','<summary>Show every changed line with OLD and NEW line numbers</summary>','',
                fence(numbered_diff((out/c['diff']).read_text())), '</details>','']
    (out/'02_code_changes.md').write_text('\n'.join(guide)+'\n')
    findings=out/'03_findings.md'
    if not findings.exists():
        findings.write_text(f'# {name}: findings and your notes\n\n[Timeline](01_timeline.md) · [Code changes](02_code_changes.md)\n\nStatus: **manual analysis pending**. Extraction is not scientific annotation.\n\n## Your inspection notes\n\n### F001 — Working title\n\n- Sequence: event IDs.\n- Observed evidence: exact message/action/result.\n- Interpretation: what might explain it?\n- Alternative explanation: what else could account for it?\n- Next check: what would distinguish the explanations?\n- Confidence/status: open, supported, contradicted, or uncertain.\n')
    source_types=dict(collections.Counter(o.get('type','missing_type') for o in stream_records(raw)))
    manifest=dict(schema_version=1,sample_id=rec['sample_id'],source_run=str(source),backend=rec['backend'],model=rec['model'],
        replicate_seed=rec['replicate_seed'],experiment_id=rec['experiment_id'],git_head=rec['git_head'],
        generated_date=rec.get('organized_date','2026-10-10'),review_status=rec['review_status'],copied=copied,
        configured_effort=rec.get('configured_effort') or rec['config']['approach']['backend'].get('reasoning_effort'),
        matched_gpt_sample_id=rec.get('matched_gpt_sample_id'),matching_settings=rec.get('matching_settings'),
        settings_reference_sample_id=rec.get('settings_reference_sample_id'),pairing_note=rec.get('pairing_note'),
        controller_review=rec.get('controller_review'),
        source_stream_types=source_types,raw_lines=len(raw.splitlines()),completed_items=len(completed),
        timeline_entries=len(events),saved_head_commits=len(commits),
        saved_all_ref_commits=int(git('rev-list','--count','--all').decode()),
        policy_changing_commits=sum('approach.py' in c['files'] for c in commits),
        history_bundle_sha256=sha(bundle.read_bytes()),
        generated_documents={name:sha((out/name).read_bytes()) for name in ('01_timeline.md','02_code_changes.md')},
        scope='Saved stream and Git history extracted; no archived code executed. Claude inline helper records retain actor identity; Codex separate helper session trees are not fully merged. Background launches are not treated as finished jobs. Full original session records remain at source. Findings are separate manual work.')
    if rec['backend']=='claude':
        manifest['claude_coverage']={k:v for k,v in coverage.items() if k not in ('coverage','raw_only')}
    dump(evdir/'manifest.json',manifest)
    print(json.dumps(dict(run=rec['run_id'],events=len(completed),commits=len(commits),status=rec['review_status'])))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',help='sample_id from runs.json; omit to organize every registered run')
    args=parser.parse_args();registry=json.loads((ROOT/'runs.json').read_text())
    selected=[r for r in registry['records'] if not args.run or r['sample_id']==args.run]
    if not selected:parser.error('Unknown run')
    for rec in selected:build(rec)
