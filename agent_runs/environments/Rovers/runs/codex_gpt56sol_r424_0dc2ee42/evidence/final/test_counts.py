import sys
from env_client import make_env
from approach import GeneratedApproach

start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
stop = int(sys.argv[2]) if len(sys.argv) > 2 else 5
for count in (1, 2, 3, 4):
    for seed in range(start, stop):
        env = make_env()
        try:
            state, info = env.reset(seed=seed, options={"object_count": count})
        except TypeError as exc:
            print("options unsupported", exc); env.close(); raise SystemExit
        app = GeneratedApproach(env.action_space, env.observation_space, {})
        app.reset(state, info)
        done = False
        for step in range(180):
            state, _, done, trunc, _ = env.step(app.get_action(state))
            if done or trunc:
                break
        print(count, seed, done, step + 1, app.phase, flush=True)
        env.close()
