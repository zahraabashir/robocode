"""Validate the self-contained reading structure without running archived code."""
from pathlib import Path
import collections
import hashlib
import json
import re
import subprocess
import tempfile
import zipfile
from build_inspection import stream_records

ROOT=Path(__file__).resolve().parents[1]


def sha(data):return hashlib.sha256(data).hexdigest()


def need(condition,message):
    if not condition:raise AssertionError(message)


def unfenced(text):
    result=[];marker=None
    for line in text.splitlines():
        m=re.match(r'^\s*(`{3,}|~{3,})',line)
        if m:
            value=m.group(1)
            if marker is None:marker=value
            elif value[0]==marker[0] and len(value)>=len(marker):marker=None
            continue
        if marker is None:result.append(line)
    return '\n'.join(result)


def verify_claude(raw,events,audit):
    """Check normalized pointers independently against the source, block by block."""
    def blocks(o):
        c=o.get('message',{}).get('content',[])
        return c if isinstance(c,list) else [{'type':'text','text':c}]
    expected=set();requests={};responses={}
    for line,o in enumerate(raw,1):
        if o.get('type') in ('assistant','user'):
            for index,b in enumerate(blocks(o),1):
                expected.add((line,index))
                key=(o.get('session_id'),b.get('id') if b.get('type')=='tool_use' else b.get('tool_use_id'))
                if b.get('type')=='tool_use':requests[key]=(line,index,b)
                if b.get('type')=='tool_result':responses[key]=(line,index,b)
        else:expected.add((line,None))
    ledger=audit['coverage']+audit['raw_only']
    need(collections.Counter((v['line'],v['block']) for v in ledger)==collections.Counter(expected),'Claude ledger coverage mismatch')
    byid={e['id']:e for e in events};byloc={(e['source_line'],e['source_block']):e for e in events}
    need(len(byloc)==len(events),'Repeated Claude source location')
    session=0
    for line,o in enumerate(raw,1):
        if o.get('type')=='system' and o.get('subtype')=='init':session+=1
        for e in [v for k,v in byloc.items() if k[0]==line]:
            index=e['source_block'];b=blocks(o)[index-1] if index else o
            suffix=f'B{index:02d}' if index and len(blocks(o))>1 else ''
            need(e['id']==f'E{line:04d}'+suffix,'Claude event ID mismatch')
            need(e['source_payload']==b,'Claude source content mismatch')
            need(e['parent_tool_use_id']==o.get('parent_tool_use_id'),'Claude helper attribution mismatch')
            need(e['session_id']==o.get('session_id') and e['turn']==session,'Claude session mismatch')
            if index and b.get('type')=='text':need(e['item']['text']==b.get('text',''),'Claude text changed')
    for key,(line,index,b) in responses.items():
        need((line,index) in byloc,'Missing Claude response')
        e=byloc[line,index];req=requests.get(key)
        need(e['start_line']==(req[0] if req else None),'Claude request pairing mismatch')
        need(e['request_payload']==(req[2] if req else None),'Claude request content mismatch')
        c=b.get('content','')
        output=c if isinstance(c,str) else ('\n'.join(v.get('text','') if v.get('type')=='text' else json.dumps(v,ensure_ascii=False) for v in c) if isinstance(c,list) else json.dumps(c,ensure_ascii=False))
        need(e['item']['aggregated_output']==output,'Claude result text changed')
    for v in audit['coverage']:
        need(v['event'] in byid,'Claude ledger references missing event')
        e=byid[v['event']]
        if v['role']=='tool_request':
            need(v['line']==e['start_line'],'Claude request ledger mismatch')
        else:need((v['line'],v['block'])==(e['source_line'],e['source_block']),'Claude result ledger mismatch')
    for v in audit['raw_only']:
        o=raw[v['line']-1];index=v['block']
        if index:
            b=blocks(o)[index-1]
            need(b.get('type')=='thinking' and not b.get('thinking'),'Readable content omitted')
        else:need(o.get('type')=='tool_progress' or (o.get('type')=='system' and o.get('subtype') in ('task_progress','background_tasks_changed','task_updated')),'Non-progress metadata omitted')
    for key,(line,index,b) in requests.items():
        if key not in responses:need(byloc[line,index]['kind']=='unfinished_item','Unreturned request omitted')


def verify():
    registry=json.loads((ROOT/'runs.json').read_text())
    inventory=json.loads((ROOT/'migration/legacy_inventory.json').read_text())
    backup=ROOT/'migration'/inventory['backup'];old_unchanged=0;old_absent=0;old_changed=[]
    with zipfile.ZipFile(backup) as z:
        need(len(z.namelist())==len(inventory['files']),'Backup entry coverage mismatch')
        for f in inventory['files']:
            data=z.read(f['path'])
            need(sha(data)==f['sha256'] and len(data)==f['bytes'],'Backup hash mismatch: '+f['path'])
            p=ROOT/f['path']
            if not p.exists():old_absent+=1
            elif sha(p.read_bytes())==f['sha256']:old_unchanged+=1
            else:old_changed.append(f['path'])
    reports=[];hashes=set();runids=set();all_links=0
    for rec in registry['records']:
        out=ROOT/rec['directory'];evidence=out/'evidence'
        manifest=json.loads((evidence/'manifest.json').read_text())
        need(rec['run_id'] not in runids,'Duplicate folder identity');runids.add(rec['run_id'])
        need(rec['stream_sha256'] not in hashes,'Repeated source transcript needs identity review');hashes.add(rec['stream_sha256'])
        for c in manifest['copied']:
            need(sha((out/c['copy']).read_bytes())==c['sha256'],'Copy changed: '+c['copy'])
            need(sha(Path(c['source']).read_bytes())==c['sha256'],'Source changed: '+c['source'])
        need(sha((evidence/'stream.jsonl').read_bytes())==rec['stream_sha256'],'Transcript identity mismatch')
        events=json.loads((evidence/'events.json').read_text())
        raw=stream_records((evidence/'stream.jsonl').read_text())
        actual=[e for e in events if e['kind']=='completed_item']
        if rec['backend']=='claude':
            verify_claude(raw,events,json.loads((evidence/'stream_coverage.json').read_text()))
        else:
            expected={i:obj['item'] for i,obj in enumerate(raw,1) if obj.get('type')=='item.completed'}
            need({e['source_line']:e['item'] for e in actual}==expected,'Completed event coverage mismatch')
            nonjson={i:o for i,o in enumerate(raw,1) if o.get('type')=='non_json_record'}
            need({e['source_line']:e['item'] for e in events if e['item'].get('type')=='non_json_record'}==nonjson,'Non-JSON lines lost or moved')
        need(len({e['id'] for e in events})==len(events),'Duplicate event IDs')
        for e in events:
            if rec['backend']!='claude':need(e['id']==f"E{e['source_line']:04d}",'Unstable event ID')
        # Identity comes from config, not from a folder or an earlier message.
        conf=subprocess.check_output(['/usr/bin/ruby','-rjson','-ryaml','-e',
            'puts JSON.generate(YAML.safe_load(File.read(ARGV[0]), permitted_classes: [], aliases: true))',str(evidence/'config.yaml')])
        conf=json.loads(conf)
        need(conf['approach']['backend']['model']==rec['model'],'Model/config mismatch')
        need(conf['approach']['backend']['backend']==rec['backend'],'Backend/config mismatch')
        need(conf['replicate_seed']==rec['replicate_seed'],'Replicate/config mismatch')
        if rec.get('configured_effort'):
            bk=conf['approach']['backend'];need(bk.get('effort',bk.get('reasoning_effort'))==rec['configured_effort'],'Effort/config mismatch')
        reference=rec.get('matched_gpt_sample_id') or rec.get('settings_reference_sample_id')
        if reference:
            partner=next(r for r in registry['records'] if r['sample_id']==reference)
            need(partner['environment_name']==rec['environment_name'],'Reference environment mismatch')
            if rec.get('matched_gpt_sample_id'):need(partner['replicate_seed']==rec['replicate_seed'],'Pair replicate mismatch')
            paired=json.loads(subprocess.check_output(['/usr/bin/ruby','-rjson','-ryaml','-e',
                'puts JSON.generate(YAML.safe_load(File.read(ARGV[0]), permitted_classes: [], aliases: true))',str(ROOT/partner['directory']/'evidence/config.yaml')]))
            for key,same in rec['matching_settings'].items():
                a,b=conf,paired
                for part in key.split('.'):a,b=a[part],b[part]
                need(same is True and a==b,'Pair settings differ: '+key)
            need((evidence/'task.md').read_bytes()==(ROOT/partner['directory']/'evidence/task.md').read_bytes(),'Pair task text differs')
            need(conf['approach']['load_dir'] is None,'Reevaluation needs lineage review')
        commits=json.loads((evidence/'commits.json').read_text())
        bundle=evidence/'history.bundle'
        need(sha(bundle.read_bytes())==manifest['history_bundle_sha256'],'Bundle changed')
        with tempfile.TemporaryDirectory(prefix='agent_runs_verify_') as d:
            repo=Path(d)/'restored.git'
            subprocess.run(['git','-c','core.hooksPath=/dev/null','clone','--bare',str(bundle),str(repo)],capture_output=True,check=True)
            def git(*args):return subprocess.check_output(['git','--no-optional-locks','-C',str(repo),*args],stderr=subprocess.PIPE)
            git('fsck','--full','--no-reflogs')
            saved=git('rev-list','--reverse','--topo-order',rec['git_head']).decode().splitlines()
            need(saved==[c['commit'] for c in commits],'Commit coverage/order mismatch')
            need(len(saved)==manifest['saved_head_commits'],'Commit count mismatch')
            need(int(git('rev-list','--count','--all'))==manifest['saved_all_ref_commits'],'All-ref history mismatch')
            need(sha(git('show',rec['git_head']+':approach.py'))==rec['policy_sha256'],'Final bundled policy mismatch')
            for i,c in enumerate(commits,1):
                need(c['id']==f'C{i:03d}','Commit ID mismatch')
                need(sha((out/c['diff']).read_bytes())==c['diff_sha256'],'Saved diff changed')
                expected_diff=git('show','--format=','--no-ext-diff','--no-textconv','--root',c['commit']).decode(errors='replace')
                need((out/c['diff']).read_text()==expected_diff,'Diff/bundle mismatch')
                if c.get('version'):
                    code=(out/c['version']).read_bytes()
                    need(sha(code)==c['policy_sha256'],'Policy snapshot changed')
                    need(code==git('show',c['commit']+':approach.py'),'Policy/bundle mismatch')
                for m in c['events']:need(m['event'] in {e['id'] for e in events},'Broken commit/event mapping')
        for name,expected_hash in manifest['generated_documents'].items():
            need(sha((out/name).read_bytes())==expected_hash,'Generated file changed since build: '+str(out/name))
        need((out/'03_findings.md').is_file(),'Missing human notes document')
        reports.append(dict(sample_id=rec['sample_id'],backend=rec['backend'],directory=rec['directory'],completed_events=len(actual),
                            helper_events=sum(bool(e.get('parent_tool_use_id')) for e in events),
                            commits=len(commits),policy_snapshots=sum(bool(c.get('version')) for c in commits),
                            review_status=rec['review_status'],bundle_restore='passed',source_hashes='passed'))
    # Check only live reading documents; historical markdown inside the backup is inert.
    docs=[ROOT/'README.md',ROOT/'protocol.md',ROOT/'migration/README.md',*sorted((ROOT/'environments').rglob('*.md'))]
    # Previous helper excerpts are literal historical data and have no active links.
    legacy_roots={p.split('/')[0] for p in inventory['legacy_roots']}
    link_errors=[];document_cache={};anchor_cache={}
    def document(path):
        if path not in document_cache:document_cache[path]=unfenced(path.read_text())
        return document_cache[path]
    def anchors(path):
        if path not in anchor_cache:
            content=document(path)
            ids=set(re.findall(r'<a\s+id="([^"]+)"',content))
            for heading in re.findall(r'^#{1,6}\s+(.+)$',content,re.M):
                ids.add(re.sub(r'[^\w -]','',heading.lower()).replace(' ','-'))
            anchor_cache[path]=ids
        return anchor_cache[path]
    for doc in docs:
        content=document(doc)
        for target in re.findall(r'\]\(([^)]+)\)',content):
            target=target.strip('<>')
            if re.match(r'^[a-zA-Z]+://',target):continue
            path,_,anchor=target.partition('#')
            dest=(doc.parent/path).resolve() if path else doc.resolve()
            # The verification report is written after these checks.
            if dest==ROOT/'migration/verification.json':continue
            if not dest.exists():link_errors.append(f'{doc.relative_to(ROOT)} -> missing {target}');continue
            if dest.is_relative_to(ROOT) and dest.relative_to(ROOT).parts[0] in legacy_roots:
                link_errors.append(f'{doc.relative_to(ROOT)} -> legacy dependency {target}')
            if anchor and dest.suffix=='.md':
                if anchor not in anchors(dest):link_errors.append(f'{doc.relative_to(ROOT)} -> missing anchor {target}')
            all_links+=1
    need(not link_errors,'\n'.join(link_errors))
    report=dict(status='passed',date=registry['snapshot_date'],runs=reports,
        total_completed_events=sum(r['completed_events'] for r in reports),
        total_commits=sum(r['commits'] for r in reports),
        total_policy_snapshots=sum(r['policy_snapshots'] for r in reports),
        backup=dict(files=len(inventory['files']),sha256=sha(backup.read_bytes()),
                    files_still_unchanged_at_old_locations=old_unchanged,files_absent_at_old_locations=old_absent,
                    old_files_changed_since_backup=old_changed),
        checked_live_links=all_links,legacy_reading_dependencies=0,
        archive_code_executed=False,original_archive_modified=False,
        scope='Hash equality for copied source files; Codex completed items and Claude block-by-block coverage, request/result pairing and actor attribution; all HEAD commits and saved refs restored from bundles; policy snapshots/diffs; live links. Counts describe extraction units, not comparable decisions across providers. Does not independently validate scientific interpretations or exhaustively copy backend/media trees.')
    (ROOT/'migration/verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('runs','scope')},indent=2))


if __name__=='__main__':verify()
