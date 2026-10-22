import sys
from env_client import make_env
from approach import GeneratedApproach


def run(seed, verbose=False):
    env = make_env()
    obs, info = env.reset(seed=seed)
    app = GeneratedApproach(env.action_space, env.observation_space, env.make_primitives())
    app.reset(obs, info)
    total = 0
    term = trunc = False
    for step in range(env.max_steps):
        obs, rew, term, trunc, info = env.step(app.get_action(obs))
        total += rew
        if term or trunc:
            break
    if verbose or not term:
        print(seed, term, trunc, step + 1, total, info, app.phase)
        if not term:
            for typ in ("rover", "objective", "sample"):
                for ob in obs.get_objects(app.types[typ]):
                    feats = app.space.type_features[ob.type]
                    print(ob.name, {f: float(obs.get(ob, f)) for f in feats})
    env.close()
    return term, step + 1


if __name__ == "__main__":
    seeds = [int(x) for x in sys.argv[1:]] or list(range(10))
    out = [run(s) for s in seeds]
    print("SUMMARY", sum(x[0] for x in out), "/", len(out), out)
