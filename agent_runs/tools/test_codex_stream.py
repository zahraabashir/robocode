"""Preserve source IDs when launcher text appears in an otherwise JSONL stream."""
import json
import unittest
from build_inspection import normalize,stream_records


class CodexStreamTests(unittest.TestCase):
    def test_noise_and_unfinished_tools_keep_original_lines(self):
        raw='Firewall initialized: outbound restricted to whitelisted domains.\n'+ '\n'.join(json.dumps(o) for o in [
            {'type':'turn.started'},
            {'type':'item.started','item':{'id':'a','type':'command_execution','command':'example'}},
            {'type':'item.completed','item':{'id':'a','type':'command_execution','command':'example','aggregated_output':'saved','exit_code':0}},
            {'type':'item.started','item':{'id':'b','type':'command_execution','command':'unfinished'}}])
        events=normalize(raw)
        self.assertEqual([e['id'] for e in events],['E0001','E0002','E0004','E0005'])
        self.assertEqual(events[0]['item']['text'],raw.splitlines()[0])
        self.assertEqual(events[2]['start_line'],3)
        self.assertEqual(events[3]['kind'],'unfinished_item')

    def test_truncated_json_is_retained_for_review(self):
        raw='{"type":"item.completed",\n\n'
        rows=stream_records(raw)
        self.assertEqual([o['text'] for o in rows],raw.splitlines())
        self.assertTrue(all(e['kind']=='unrecognized' for e in normalize(raw)))


if __name__=='__main__':unittest.main()
