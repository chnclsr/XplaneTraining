import gym
import numpy as np
from Discrete_SAC_Agent import SACAgent
import os
import gym_xplane
import wandb

TRAINING_EVALUATION_RATIO = 4
RUNS = 5
EPISODES_PER_RUN = 400
STEPS_PER_EPISODE = 200

if __name__ == "__main__":
    print("initialize Wandb")
    os.environ["WANDB_MODE"] = "online"
    os.environ["WANDB_API_KEY"] = "48454db87872b0da16c749491c7e362e5933ceee"
    user = "calisircihan21"
    project = "XPlane11"
    display_name = "Xplane11Training_SAC_1"
    wandb.init(entity=user, project=project, name=display_name)

    env = gym.make("gymXplane-v2")
    agent_results = []

    agent = SACAgent(env)
    run_results = []
    for episode_number in range(EPISODES_PER_RUN):
        evaluation_episode = episode_number % TRAINING_EVALUATION_RATIO == 0
        episode_reward = 0
        state = env.reset()
        done = False
        i = 0
        while not done and i < STEPS_PER_EPISODE:
            print('\r', f'Episode: {episode_number + 1} timestep: {i}', end=' ')
            i += 1
            action = agent.get_next_action(state, evaluation_episode=evaluation_episode)
            next_state, reward, done, info = env.step(action)
            if not evaluation_episode:
                agent.train_on_transition(state, action, next_state, reward, done)
            else:
                episode_reward += reward
            state = next_state
        if evaluation_episode:
            run_results.append(episode_reward)
            print("Avg. score for last 100 episode: ", np.mean(run_results[-100:]))
            wandb.log({"episode_reward": episode_reward, "episode": episode_number})

    env.close()


