from env_client import make_env


def dump(seed, object_count=None):
    env = make_env()
    kwargs = {"seed": seed}
    if object_count is not None:
        # reset may or may not expose this option; keep ordinary seeded resets primary.
        kwargs["options"] = {"object_count": object_count}
    try:
        state, info = env.reset(**kwargs)
        print("SEED", seed, "COUNT_ARG", object_count, "MAX", env.max_steps,
              "ASHAPE", env.action_space.shape,
              "LOW", env.action_space.low.tolist(), "HIGH", env.action_space.high.tolist(),
              "INFO", info)
        for name in state.get_object_names():
            obj = state.get_object_from_name(name)
            feats = env.observation_space.type_features[obj.type]
            vals = {f: float(state.get(obj, f)) for f in feats}
            print(name, obj.type.name, vals)
    finally:
        env.close()


if __name__ == "__main__":
    for s in range(12):
        dump(s)
