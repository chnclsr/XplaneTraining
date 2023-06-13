from gym.envs.registration import register

register(
    id='gymXplane-v2',
    entry_point='gym_xplane.gym_xplane.envs.xplane_envBase:XplaneEnv',
    kwargs={'config': {"worker_index":1}}
)