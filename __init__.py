from gym.envs.registration import register

register(
    id='UnstablePendulum-v0',
    entry_point='unstable_gym.unstable_pendulum:UnstablePendulumEnv'
)

register(
    id='UnstableCartpole-v0',
    entry_point='unstable_gym.unstable_cartpole:UnstableCartPoleContEnv'
)