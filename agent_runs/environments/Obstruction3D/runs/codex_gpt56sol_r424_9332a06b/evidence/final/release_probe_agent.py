"""Focused logging of final target release on deterministic seeds."""
import sys
from env_client import make_env
from approach import GeneratedApproach


for seed in map(int, sys.argv[1:] or [0, 11]):
    env = make_env()
    state, info = env.reset(seed=seed)
    policy = GeneratedApproach(env.action_space, env.observation_space, {})
    policy.reset(state, info)
    prior = None
    for step in range(env.max_steps):
        action = policy.get_action(state)
        mode = policy.mode
        state, reward, done, trunc, info = env.step(action)
        if mode == "release" and policy.object_name == "target_block":
            robot = state.get_object_from_name("robot")
            block = state.get_object_from_name("target_block")
            vals = (
                step, policy.release_t, float(action[10]),
                state.get(robot, "finger_state"), state.get(robot, "grasp_active"),
                state.get(block, "grasp_active"), state.get(block, "pose_x"),
                state.get(block, "pose_y"), state.get(block, "pose_z"),
            )
            sig = tuple(round(float(x), 5) for x in vals[3:])
            if policy.release_t <= 8 or sig != prior or policy.release_t % 10 == 0:
                print(seed, *[round(float(x), 5) for x in vals])
            prior = sig
        if done or trunc:
            print("RESULT", seed, step + 1, done, trunc, policy.mode)
            break
    env.close()
