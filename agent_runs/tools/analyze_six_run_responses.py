"""Read-only six-run descriptive audit, with explicit single-analyst annotations.

Run: MPLCONFIGDIR=/tmp/robocode-mpl python agent_runs/tools/analyze_six_run_responses.py
No historical commands or policies are executed. Source archive is never written.
Extraction proposes evidence; manual annotations classify actions, not motives.
"""
from __future__ import annotations
import hashlib
import json
from collections import Counter
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2] / 'agent_runs'
LABELS = {'I':'Investigate failures', 'R':'Immediate policy edit/restore',
          'B':'Broader sampling/regression', 'T':'Investigate testing capability',
          'O':'Other substantive action'}

MANUAL = json.loads(r'''
{
 "codex_gpt56sol_r424_7e89c88a": [
 ["E0034","E0036","R",0,1,"200-step capped baseline test; next action changes the controller."],
 ["E0038","E0042","R",0,3,"300-step capped test; next main-stream action edits the controller. Parallel probe results are separate information."],
 ["E0053","E0055","I",1,5,"Trace the four failed seeds, printing phases, poses and errors before editing."],
 ["E0059","E0061","I",3,6,"Trace failed seeds 0–2 with controller modes and pose errors."],
 ["E0065","E0067","I",5,6,"Trace remaining failure seed 2 before changing routing."],
 ["E0071","E0073","I",11,12,"Trace failed seed 6 and inspect wall-limited navigation."],
 ["E0081","E0084","R",0,1,"Agent states a wall/rotation explanation, then adds clearance prepositioning."],
 ["E0088","E0090","R",17,20,"Change final orientation correction before retesting 13, 15 and 19."]
 ],
 "claude_opus55_high_r424_b71e4671": [
 ["E0033","E0043","B",15,16,"Compound command: launch larger seeds 16–115 first, then request a layout dump of failed seed 4; message explicitly proposes both.","compound"],
 ["E0059","E0063","I",96,100,"First completed report from background sweep; inspect failed seeds 21 and 31."],
 ["E0225","E0231","I",29,40,"Debug failed seed 6 after the controller rewrite."],
 ["E0241","E0245","I",38,40,"Debug failed seed 5 and examine geometry before editing feasibility checks."],
 ["E0288","E0293","I",99,100,"Debug failed seed 75 and inspect its planned drop."],
 ["E0430","E0434","I",294,300,"First completed background sweep report; debug failed seed 577 before a shared repair."]
 ],
 "claude_opus55_high_r424_2a46a52d": [
 ["E0196","E0200","O",238,240,"Two of six parameter variants fail; next action traces successful default seed 200, not an identified failed case.","parameter_variants"],
 ["E0209","E0214","I",78,80,"Two failing variants identify seed 212; inspect its stalled planner with KMAX=50.","parameter_variants"]
 ],
 "codex_gpt6astra_r424_51fd524e": [
 ["E0024","E0026","R",0,5,"All five rollout results fail; immediately change contact height and storage."],
 ["E0026","E0029","R",2,5,"Two seeds pass; immediately change early-attachment detection."],
 ["E0029","E0031","I",9,10,"Read the current policy after the remaining seed-4 failure, before editing it."],
 ["E0054","E0063","R",97,100,"Wall-placement failures; however an already-running ten-seed success batch returns before the repair is launched.","competing_feedback"],
 ["E0082","E0085","I",0,1,"Seed 151 fails; a separate 200-seed batch returns before the next inspection.","competing_feedback"],
 ["E0083","E0085","I",199,201,"One targeted scene passes plus 198/200 regression successes; inspect the completed four-obstruction seed-2 result."],
 ["E0085","E0088","R",0,1,"Saved JSON contains the full one-case test (seed 2, count 4); next action repairs carried geometry."],
 ["E0088","E0091","R",3,4,"Seed 151 still fails while three count-4 cases pass; immediately reserve the final base footprint."]
 ],
 "codex_gpt6astra_r424_4e86deee": [
 ["E0028","E0030","I",0,5,"Inspect the stored trace of failed seed 0."],
 ["E0035","E0042","R",0,5,"Another policy/test call was launched before this result; its feedback arrives before a new response can be isolated.","competing_feedback"],
 ["E0039","E0042","R",1,5,"The trace inspection E0040 started before this result, so the first new action is the contact-selection edit."],
 ["E0059","E0066","R",39,40,"First complete failure report for seeds 20–59: producer E0055 ended, grep identifies seed 35 as the only failure, and tail reaches seed 59. Repair endpoints next."],
 ["E0066","E0068","R",12,17,"Inspect E0065 was already launched before this feedback; first new action edits contact sampling."],
 ["E0134","E0145","B",299,300,"Completed main_v3 report; the agent had already stated seed 516 was repaired and had launched final sweeps. New action starts another final batch.","superseded_failure"]
 ]
}
''')


def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def summaries(output):
    result=[]
    for line in output.splitlines():
        m=re.match(r'^(?:success|solved)\s+(\d+)\s*/\s*(\d+)',line,re.I)
        if not m: m=re.match(r'^SUMMARY\s+(\d+)\s*/\s*(\d+)',line)
        if not m: m=re.match(r'^\{.*\}\s+succ\s+(\d+)\s*/\s*(\d+)',line)
        if m:
            result.append((int(m[1]),int(m[2]))); continue
        m=re.match(r'^SUMMARY\s+(\d+)\s+success\s+(\d+)',line)
        if m:result.append((int(m[2]),int(m[1])))
    return result


def policy_write(e):
    i=e['item']
    if i.get('type')=='file_change':
        return any(Path(c['path']).name=='approach.py' for c in i.get('changes',[]))
    c=i.get('command','')
    if 'approach.py' not in c:return False
    return bool(re.search(r"open\(['\"]approach\.py['\"]\s*,\s*['\"]w",c)
                or re.search(r"p\s*=\s*['\"]approach\.py['\"]",c) and re.search(r"open\(p,\s*['\"]w",c)
                or re.search(r'cat\s*>\s*approach\.py',c)
                or re.search(r'sed\s+-i[^\n]*approach\.py',c)
                or re.search(r'(?:checkout|restore)[^\n]*approach\.py',c)
                or re.search(r'>\s*approach\.py',c))


def build():
    registry=json.loads((ROOT/'runs.json').read_text())['records']
    chosen=[r for r in registry if r['replicate_seed']==424 and r['environment_name'] in ('Obstruction2D','DynPushT2D')]
    assert len(chosen)==6 and len({r['stream_sha256'] for r in chosen})==6
    data=[]
    for r in chosen:
        directory=ROOT/r['directory'];events=json.loads((directory/'evidence/events.json').read_text());by_id={e['id']:e for e in events}
        audits=[]
        for e in events:
            i=e['item'];o=i.get('aggregated_output','');ss=summaries(o)
            if ss and i.get('type')=='command_execution':
                audits.append({'event':e['id'],'summaries':ss,'any_failure':any(a<b for a,b in ss)})
        if r['run_id']=='codex_gpt56sol_r424_2c85c614':
            original=json.loads((directory/'evidence/test_decisions.json').read_text())
            rows=[{'event':x['event'],'next_event':x['next_event'],'label':{'D':'I','R':'R','V':'B','T':'T'}[x['label']],
                   'solved':x['solved'],'total':x['total'],'note':x['note'],'flags':[]}
                  for x in original['rows'] if x['complete_clean_command'] and x['result']=='any_failure']
            assert len(rows)==54
        else:
            rows=[]
            for line in MANUAL[r['run_id']]:
                a,b,label,solved,total,note,*flags=line
                rows.append(dict(event=a,next_event=b,label=label,solved=solved,total=total,note=note,flags=flags))
            detected={a['event'] for a in audits if a['any_failure']}
            annotated={x['event'] for x in rows}
            assert detected<=annotated,(r['run_id'],'Unreviewed summary failure',detected-annotated)
        # Completed-feedback boundaries include pass batches as well as failures.
        boundaries={x['event'] for x in rows}|{a['event'] for a in audits}
        for e in events:
            i=e['item'];c=i.get('command','');o=i.get('aggregated_output','')
            eps=re.findall(r'^(\d+)\s+(True|False|OK|FAIL)\s+\d+',o,re.M)
            if 'python test_approach.py' in c and eps and i.get('exit_code')==0:
                # Exact requested/result counts for direct test calls were checked in the manual audit.
                boundaries.add(e['id'])
        for x in rows:
            e=by_id[x['event']];n=by_id[x['next_event']];start=n.get('start_line') or n['source_line']
            assert start>e['source_line'],(r['run_id'],x['event'],'action prelaunched')
            x['feedback_source_line']=e['source_line'];x['next_action_start_line']=start
            x['outcome']='partial_success' if x['solved'] else 'complete_failure'
            x['eligible_primary']=not any(flag in x['flags'] for flag in ('competing_feedback','superseded_failure'))
            future=sorted([by_id[a] for a in boundaries if by_id[a]['source_line']>e['source_line']],key=lambda a:a['source_line'])
            boundary=future[0] if future else None
            x['next_completed_feedback']=boundary['id'] if boundary else None
            upper=boundary['source_line'] if boundary else max(a['source_line'] for a in events)
            edits=[a for a in events if e['source_line']<(a.get('start_line') or a['source_line'])<=upper and policy_write(a)]
            x['policy_edits_before_next_completed_feedback']=[a['id'] for a in sorted(edits,key=lambda a:a.get('start_line') or a['source_line'])]
            x['followup_sequence']=x['label']+(' → policy edit' if edits and x['label']!='R' else '')+(' → completed test feedback' if boundary else ' → end of record')
            # Verify a declared competing-feedback flag against observed event order.
            if boundary and boundary['source_line']<start:
                assert 'competing_feedback' in x['flags'],(r['run_id'],x['event'],boundary['id'],'unflagged competing feedback')
        data.append(dict(run_id=r['run_id'],directory=r['directory'],model=r['model'],environment=r['environment_name'],replicate_seed=424,
                         source_hashes={name:digest(directory/'evidence'/name) for name in ('events.json','stream.jsonl')},
                         rows=rows,summary_output_inventory=audits))
    return {'schema_version':1,'date':'2026-10-11','unit':'One completed main-stream policy-test command/batch feedback, not one failed episode.',
            'labeling':'Single analyst, evidence-reviewed manual labels; not blinded, not an automatic intent classifier or formal ACT*ONOMY labeling.',
            'labels':LABELS,'runs':data}


def event_link(run,event):
    p=ROOT/run['directory']/'01_timeline.md'
    n=next(i+1 for i,l in enumerate(p.read_text().splitlines()) if l==f'<a id="{event}"></a>')
    return f'[{event}]({p}:{n})'


def report(d):
    text='''# How often do agents investigate, repair, or broaden testing?

Six whole organized development streams; descriptive audit, 2026-10-11.

## Start here

The sample is fixed: **Obstruction2D and DynPushT2D × GPT-5.6-sol, GPT-6 Astra and Claude Opus 5.5 × development replicate 424**. These are six distinct registered transcripts, not reevaluation scores or repeated exports. The matching replicate number does not make episode conditions, prompts, compute budgets, model effort or task difficulty equivalent. One run per model/environment cell cannot establish model effects.

We count the first substantive action after **completed policy-test batch feedback containing at least one failed episode**. A multi-seed batch or multi-variant tuning command is one decision opportunity, even if it reports many failures. The full main development stream was screened, and each included row was checked against its commands, outputs and subsequent actions. Interrupted tests, environment initialization errors, hand-controlled physics probes, diagnostic traces and progress-only reads are outside this primary denominator. Subagent-private results are not separately counted; their influence is a limitation.

An agent can react before a background batch finishes. Such partial reports are important but require a different unit. They are documented below, not silently mixed into completed-batch counts. Repeated reads of the same saved results are not new test batches. Polling, waiting, budget queries, commits and saving outputs are skipped when identifying the next substantive action. A policy-code inspection counts as investigation; a message alone is not an executed action. In a compound command the first substantive operation determines the first-action label, with mixed operations flagged.

Three rows have intervening completed feedback before a new response can be isolated; one reports a superseded controller failure after the agent already said it was fixed. These four rows remain in the ledger but are excluded from the primary first-response percentages. Labels describe observable actions, not the agent’s internal uncertainty or causal motivations.

## First response after a failed batch

Counts below exclude the four qualified rows. Percentages use the eligible failures in each row, not robot episodes. “Repair” means an immediate controller edit or restore attempt; success of the edit is a separate question.

| Environment | Model | Failed batches recorded | Eligible | Investigate | Immediate edit | Broaden tests | Testing capability | Other |
|---|---|---:|---:|---:|---:|---:|---:|---:|
'''
    totals=Counter();eligible_all=[]
    ordered=sorted(d['runs'],key=lambda r:(r['environment'],{'gpt-5.6-sol':0,'gpt-6-astra':1,'claude-opus-5-5':2}[r['model']]))
    for r in ordered:
        rows=[x for x in r['rows'] if x['eligible_primary']];c=Counter(x['label'] for x in rows);totals.update(c);eligible_all.extend(rows)
        cells=[f"{c[k]} ({c[k]/len(rows):.0%})" for k in LABELS]
        text+=f"| {r['environment']} | {r['model']} | {len(r['rows'])} | {len(rows)} | "+' | '.join(cells)+' |\n'
    text+='\nThere are **84 recorded completed failure-feedback opportunities and 80 eligible first-response rows**, after the four exclusions.\n\nThe counts are uneven: the GPT Obstruction2D run contributes most decision opportunities. A pooled percentage would therefore mostly describe that run. There are no model-wide significance tests or independent-episode confidence intervals here.\n\n'
    text+='![First-response frequencies across the six runs]('+str(ROOT/'failure_response_frequency.png')+')\n\n'
    text+='## Broader testing after partial success versus complete failure\n\n'
    text+='| Run | Broaden after partial success | Broaden after complete failure |\n|---|---:|---:|\n'
    for r in ordered:
        rows=[x for x in r['rows'] if x['eligible_primary']];cells=[]
        for outcome in ('partial_success','complete_failure'):
            a=[x for x in rows if x['outcome']==outcome];b=sum(x['label']=='B' for x in a)
            cells.append(f'{b}/{len(a)}' if a else 'No eligible batches')
        text+=f"| {r['environment']} · {r['model']} | {' | '.join(cells)} |\n"
    text+='''
This comparison concerns **the reported batch outcome**, not all unresolved failures from earlier work. Three GPT Obstruction2D broader-testing rows follow mixed success; the Claude Obstruction2D row also follows mixed success but combines a broad sweep and a same-case dump in one command. Removing that compound row leaves three clear broader-first switches. These are few events, so the pattern is a hypothesis lead, not a statistical law. The testing-capability row is separate: its next action is inspection of reset options before expansion.

## What happens after investigation?

We checked whether the main controller file was visibly edited after the investigation and before the next completed batch feedback. This describes sequence order only: it does not show that the edit fixes the diagnosed cause, and asynchronous batches may have started earlier. Changes to auxiliary modules can be missed by this narrower main-controller measure.

| Run | Investigation first | Followed by a main-controller edit before next completed feedback |
|---|---:|---:|
'''
    for r in ordered:
        a=[x for x in r['rows'] if x['eligible_primary'] and x['label']=='I'];b=sum(bool(x['policy_edits_before_next_completed_feedback']) for x in a)
        text+=f"| {r['environment']} · {r['model']} | {len(a)} | {b}/{len(a)} |\n"
    text+='''
Investigation and repair are consequently not alternatives over an entire trajectory. We classify their **order**. The event ledger lets you check which investigations lead to an edit and which instead lead to another test.

## What the comparison does and does not support

- Investigation-first and immediate-edit responses both recur in multiple runs.
- Broader testing as the very next action after completed failure feedback is uncommon in this selected sample. It should not be described as a common cross-model failure response from these counts.
- Claude DynPushT2D has only two completed failure batches, both involving parameter variants; its saved/default controller passes extensive tests. One next action profiles a successful default case, while the other traces the identified failed case. This is not evidence of a stable Claude failure-response preference.
- The most useful preliminary contrast is **investigate → edit → test** versus **edit → test**, together with a few broader-first switches after partial success. This warrants additional manual replication if that contrast interests you; it does not yet test an uncertainty explanation.

Before paid interventions, add another fixed replicate for these same six cells and check whether the categories and differences survive. Record outcome composition, development stage, test instrumentation and available budget; messages can supply stated explanations, but missing explanations remain unobserved.

## Important excluded or qualified evidence

- GPT Obstruction2D E0426 mixes a completed count-4 failure batch with a count-5 initialization error. The previous audit excludes it from its 54 clean failure batches; adding it contributes one investigation-first row.
- GPT DynPushT2D E0034/E0038 use 200/300-step development caps. They remain failure observations under their stated test limits, not failures under the final 1,000-step protocol.
- Astra Obstruction2D E0067 exposes seed 42/count 3 from a saved larger batch without a full aggregate; E0129 and E0147 expose failures while a long sweep is ongoing. E0183 states that a dense case stalled, followed by a bounded diagnostic at E0186. These are real evidence but outside completed-batch counts. E0085 is different: it contains the full JSON list for a one-case batch, and is included.
- Astra DynPushT2D E0097 exposes seed 608 before that batch finishes; the next new action profiles successful but slow seed 137, then a controller edit also repairs 608. E0127 mixes completed successful batches with a still-running failing batch; the completed failing aggregate first appears at E0134, after the agent has already said seed 516 was repaired. It is excluded from primary first-response percentages.
- Background log reads and stored summaries may appear repeatedly. For example, Astra Obstruction2D E0124 rereads already reported completed results; Astra DynPushT2D E0103/E0130 repeat failures from unchanged saved logs. They are not additional failure decisions.
- Claude Obstruction2D E0043 launches a broad sweep before dumping the failed seed in the same shell call. Its next-action label is B under the explicit operation-order rule, with a compound flag; a stricter sensitivity analysis removes it.

## Every included failure feedback and follow-up

Open a feedback event, then its next action, then the listed controller-edit events. Personal notes in the run-specific `03_findings.md` files have not been changed.

'''
    for r in ordered:
        text+=f"### {r['environment']} · {r['model']} · replicate 424\n\n| Feedback | Passes/total | First action | Next event | Later controller edits before next completed feedback | Note / qualifications |\n|---|---:|---|---|---|---|\n"
        for x in r['rows']:
            label=LABELS[x['label']]+(' (excluded from primary)' if not x['eligible_primary'] else '')
            edits=', '.join(event_link(r,a) for a in x['policy_edits_before_next_completed_feedback']) or 'None recorded in window'
            note=x['note']+(' Flags: '+', '.join(x['flags']) if x['flags'] else '')
            text+=f"| {event_link(r,x['event'])} | {x['solved']}/{x['total']} | {label} | {event_link(r,x['next_event'])} | {edits} | {note} |\n"
        text+='\n'
    text+='''## Reproduction and scope

`agent_runs/tools/analyze_six_run_responses.py` reads the existing normalized evidence and reproduces this note and its JSON ledger. The action labels are explicitly embedded manual annotations, not inferred motives. The JSON records source hashes, eligibility flags, every included row and an inventory of summary-bearing command outputs. That inventory is a search aid, not a count of independent test batches. The existing GPT Obstruction2D labels are reused from its audited `evidence/test_decisions.json`.

No archived shell command, historical instruction, policy or environment client was executed. No new agent generations or rollouts were run. The source experiment archive was unchanged. This is a single-analyst descriptive audit with no independent label validation yet.
'''
    (ROOT/'failure_response_frequency.md').write_text(text)
    return ordered


def figure(runs):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(figsize=(10,4.8));colors=['#3978ad','#e49545','#5c9b77','#a475b5','#8d9299'];names=[]
    for j,r in enumerate(runs):
        rows=[x for x in r['rows'] if x['eligible_primary']];c=Counter(x['label'] for x in rows);left=0
        for label,color in zip(LABELS,colors):
            width=100*c[label]/len(rows)
            ax.barh(j,width,left=left,color=color,label=LABELS[label] if j==0 else None)
            if c[label]:ax.text(left+width/2,j,str(c[label]),ha='center',va='center',color='white',fontsize=10)
            left+=width
        names.append(f"{r['environment']} · {r['model']} (n={len(rows)})")
    ax.set_yticks(range(len(names)),names);ax.invert_yaxis();ax.set_xlim(0,100);ax.set_xlabel('First action after eligible completed failure feedback (%)')
    ax.set_title('Six development runs: first response to failure\nCounts shown inside bars; replicate 424 only',loc='left',fontsize=12)
    ax.legend(loc='upper center',bbox_to_anchor=(.35,-.18),ncol=3,frameon=False,fontsize=8)
    fig.subplots_adjust(left=.40,right=.98,top=.82,bottom=.25)
    fig.savefig(ROOT/'failure_response_frequency.png',dpi=180)
    plt.close(fig)


if __name__=='__main__':
    d=build();ordered=report(d)
    (ROOT/'failure_response_frequency.json').write_text(json.dumps(d,indent=2)+'\n')
    figure(ordered)
    for r in ordered:
        rows=[x for x in r['rows'] if x['eligible_primary']]
        print(r['environment'],r['model'],'recorded',len(r['rows']),'eligible',len(rows),dict(Counter(x['label'] for x in rows)))
