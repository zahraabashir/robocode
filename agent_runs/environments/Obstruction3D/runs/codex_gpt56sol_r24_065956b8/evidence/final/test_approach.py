from env_client import make_env
from approach import GeneratedApproach

def run(seed, count=None, limit=200):
    env = make_env()
    options = {} if count is None else {"object_count": count}
    state, info = env.reset(seed=seed, options=options)
    policy = GeneratedApproach(env.action_space, env.observation_space, env.make_primitives())
    policy.reset(state, info)
    for step in range(limit):
        state, reward, terminated, truncated, info = env.step(policy.get_action(state))
        if terminated or truncated:
            env.close(); return terminated, step + 1
    env.close(); return False, limit

if __name__ == "__main__":
    for seed in range(5):
        print(seed, run(seed))
