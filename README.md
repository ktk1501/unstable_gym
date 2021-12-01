# Benchmark for Robustness Tests of Control Alrogithms

This repository contains classical control benchmarks for evaluating robustnesses of control and reinforcement learning algorithms. It can be used as zero-shot control performance evaluations. It is built upon OpenAI Gym.

# Installation

Clone repository, then 'pip install -e .' or 'pip3 install -e .' based on your environment.

Or you can manually install dependencies:

    - numpy
    - gym

# How to Run Example

You can run our test example by:

For pendulum,
```bash
python unstable_pendulum.py
```
For cartpole(continuous action),
```bash
python unstable_cartpole_cont.py
```

It's an inverted pendulum in gym environment. The sample results of the two different winds are shown below:

|                                                              Sine wave side wind                                                               |                                                                Random side wind                                                                |
| :--------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------: |
| <img src="https://user-images.githubusercontent.com/40379815/143234809-686f1395-2bac-4d33-a5c8-910c6c9bf9aa.gif" width="200px" height="200px"> | <img src="https://user-images.githubusercontent.com/40379815/143234945-3585a0bf-eb56-4c94-9a54-72bab8169c79.gif" width="200px" height="200px"> |

It's a cartpole (continuous action) environment. The sample results of the two different winds are shown below:

|                                                              Sine wave side wind                                                               |                                                                Random side wind                                                                |
| :--------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------: |
| <img src="https://user-images.githubusercontent.com/95032544/144069804-4770f193-6802-4f4f-baa3-f355a764ae1e.gif" width="300px" height="200px"> | <img src="https://user-images.githubusercontent.com/95032544/144069981-e63dbaea-0acb-4cc1-b457-ee1bd068672f.gif" width="300px" height="200px"> |

# How to Use

Simply import environments from 'unstable_gym'. For examples, for [inverted pendulum](https://github.com/ktk1501/unstable_gym/blob/master/unstable_pendulum.py):

```python
from unstable_gym.unstable_pendulum import UnstablePendulumEnv
env = UnstablePendulumEnv(wind_type="sine", max_wind=1.0)

obs = env.reset()
for step in range(500):
    action = env.action_space.sample()
    nobs, reward, done, info = env.step(action)
    env.render()
```
For [cartpole](https://github.com/ktk1501/unstable_gym/blob/master/unstable_cartpole_cont.py):

```python
from unstable_gym.unstable_cartpole_cont import UnstableCartPoleContEnv
env = UnstableCartPoleContEnv(wind_type="sine", max_wind=1.0)

for ep in range(10):
    obs = env.reset()
    for step in range(1000):
        action = env.action_space.sample()
        nobs, reward, done, info = env.step(action)
        env.render()
        if done:
            break
```
There are two options for "wind type":

1.  **"sine"** : sine wave side wind
2.  **"random"** : random side wind

You can also adjust the magnitude of the side wind (in [N]): "max_wind"

# Related Works

You can test the robustness of [MPPI](https://github.com/UM-ARM-Lab/pytorch_mppi) and [Smooth_MPPI](https://github.com/ktk1501/smooth-mppi-pytorch)
