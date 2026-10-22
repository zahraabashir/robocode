from env_client import make_env
import numpy as np


def main():
    for seed in range(10):
        env = make_env()
        obs, _ = env.reset(seed=seed)
        print(seed, "block", np.round(obs[0:3], 3), "robot", np.round(obs[16:18], 3),
              "goal", np.round(obs[29:32], 3), "dims", np.round(obs[12:15], 3),
              "r", round(float(obs[28]), 3))
        env.close()


if __name__ == "__main__":
    main()
