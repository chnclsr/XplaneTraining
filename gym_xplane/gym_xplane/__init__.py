from gym.envs.registration import register

register(
    id='gymXplane-v2',
    entry_point='gym_xplane.gym_xplane.envs.xplane_envBase:XplaneEnv',
    kwargs={'clientAddr': '0.0.0.0', 'xpHost':'127.0.0.1', 'xpPort':49009, 'clientPort':8080, 'timeout':3000, 'max_episode_steps':2000,'test':False}
)