"""Provenance edge cases; synthetic records only, no archived code execution."""
import json
import unittest
from claude_stream import normalize_claude
from verify_inspection import verify_claude


def msg(role,content,session='s1',**kw):
    return dict(type=role,session_id=session,message={'content':content},**kw)


def call(id,name='Bash',**args):return dict(type='tool_use',id=id,name=name,input=args)
def result(id,text,**kw):return dict(type='tool_result',tool_use_id=id,content=text,**kw)


class ClaudeCoverageTests(unittest.TestCase):
    def normalize(self,rows):
        events,audit=normalize_claude('\n'.join(json.dumps(x) for x in rows),lambda i:[],lambda i:i['type'])
        verify_claude(rows,events,audit)
        return events,audit

    def test_interleaved_helpers_and_multiblock_response(self):
        rows=[dict(type='system',subtype='init',session_id='s1'),
              msg('assistant',[call('main',command='test'),{'type':'text','text':'Starting'}]),
              msg('assistant',[call('helper',name='Write',file_path='test.py',content='example')],parent_tool_use_id='parent'),
              msg('user',[result('helper','saved'),{'type':'text','text':'context'}],parent_tool_use_id='parent'),
              msg('user',[result('main','running in background',is_error=False)],tool_use_result={'backgroundTaskId':'job'})]
        events,audit=self.normalize(rows)
        helper=next(e for e in events if e['id']=='E0004B01')
        self.assertEqual(helper['start_line'],3)
        self.assertEqual(helper['item']['tool_input']['content'],'example')
        self.assertEqual(helper['parent_tool_use_id'],'parent')
        main=events[-1]
        self.assertEqual(main['start_line'],2)
        self.assertIsNone(main['item']['exit_code'])
        self.assertTrue(main['item']['background_launch'])
        self.assertEqual(audit['tool_requests'],2)

    def test_sessions_empty_thinking_and_unreturned_request(self):
        rows=[dict(type='system',subtype='init',session_id='s1'),
              msg('assistant',[call('pending',command='first')]),
              msg('assistant',[{'type':'thinking','thinking':'','signature':'opaque'}]),
              dict(type='system',subtype='init',session_id='s2'),
              msg('assistant',[call('pending',command='second')],session='s2'),
              msg('user',[result('pending',[{'type':'text','text':'done'}])],session='s2')]
        events,audit=self.normalize(rows)
        first=next(e for e in events if e['id']=='E0002')
        self.assertEqual((first['kind'],first['turn']),('unfinished_item',1))
        self.assertEqual(events[-1]['start_line'],5)
        self.assertEqual(audit['thinking']['empty_readable_text'],1)

    def test_duplicate_requests_fail_loudly(self):
        rows=[msg('assistant',[call('same')]),msg('assistant',[call('same')])]
        with self.assertRaises(ValueError):self.normalize(rows)

    def test_readable_thinking_and_orphan_error_are_retained(self):
        events,audit=self.normalize([msg('assistant',[{'type':'thinking','thinking':'visible text'}]),
                                    msg('user',[result('missing','error',is_error=True)])])
        self.assertEqual(events[0]['item']['text'],'visible text')
        self.assertEqual(audit['thinking']['nonempty_readable_text'],1)
        self.assertIsNone(events[1]['request_payload'])
        self.assertTrue(events[1]['item']['tool_result_is_error'])


if __name__=='__main__':unittest.main()
