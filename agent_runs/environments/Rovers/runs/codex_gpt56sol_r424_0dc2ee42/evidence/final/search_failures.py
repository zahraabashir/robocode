import sys
from env_client import make_env
from approach import GeneratedApproach

start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
stop = int(sys.argv[2]) if len(sys.argv) > 2 else start + 50
fail = []
for seed in range(start, stop):
    env = make_env(); state, info = env.reset(seed=seed)
    app = GeneratedApproach(env.action_space, env.observation_space, {})
    app.reset(state, info)
    done = False
    for step in range(180):
        state, _, done, trunc, _ = env.step(app.get_action(state))
        if done or trunc:
            break
    env.close()
    if not done:
        fail.append((seed, app.phase, step + 1))
        print("FAIL", fail[-1], flush=True)
print("RESULT", start, stop, "failures", fail, flush=True)
