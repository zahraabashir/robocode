import sys, time
import test_approach as t
from concurrent.futures import ThreadPoolExecutor
seeds=[int(a) for a in sys.argv[1].split(',')] if ',' in sys.argv[1] else list(range(int(sys.argv[1]), int(sys.argv[2])))
cnt=int(sys.argv[3]) if len(sys.argv)>3 and sys.argv[3]!='-' else None
with ThreadPoolExecutor(int(__import__("os").environ.get("NT","2"))) as ex:
    res=list(ex.map(lambda s: (s,)+tuple(t.run(s,count=cnt)), seeds))
print(" ".join(f"{r[0]}:{r[2]}" for r in res))
for r in res:
    if not r[1]: print("FAIL", r)
print("succ", sum(r[1] for r in res), "/", len(res), "mean steps", sum(r[2] for r in res)/len(res), "max time", max(r[4] for r in res))
