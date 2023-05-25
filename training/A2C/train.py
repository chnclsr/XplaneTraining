import gym
import time
import argparse
from itertools import count
import os
import numpy as np
import torch
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
from memory import Memory
from actoc_ciritic import Actor, Critic
import wandb

parser = argparse.ArgumentParser(description='PyTorch A2C solution of CartPole-v0')
parser.add_argument('--gamma', type=float, default=0.99)
parser.add_argument('--actor_lr', type=float, default=1e-4)
parser.add_argument('--critic_lr', type=float, default=5e-4)
parser.add_argument('--batch_size', type=int, default=512)
parser.add_argument('--max_episode', type=int, default=500)

cfg = parser.parse_args()
env = gym.make('gymXplane-v2')
last_scores = []


def get_action(state):
    action_probs = actor(state)
    action_dist = torch.distributions.Categorical(action_probs)
    action = action_dist.sample()
    return action


def get_state_value(state):
    state_value = critic(state)
    return state_value


def update_actor(states, actions, advantages):
    action_probs = actor(states)
    action_dist = torch.distributions.Categorical(action_probs)
    act_loss = -action_dist.log_prob(actions) * advantages
    entropy = action_dist.entropy()
    loss = torch.mean(act_loss - 1e-4 * entropy)
    actor_optimizer.zero_grad()
    loss.backward()
    actor_optimizer.step()
    return


def update_critic(states, targets):
    state_value = critic(states)
    loss = F.mse_loss(state_value, targets)
    critic_optimizer.zero_grad()
    loss.backward()
    critic_optimizer.step()
    return


actor = Actor(env)
critic = Critic(env)
actor_optimizer = optim.Adam(actor.parameters(), lr=cfg.actor_lr)
critic_optimizer = optim.Adam(critic.parameters(), lr=cfg.critic_lr)
memory = Memory(10000)


def main():
    print("initialize Wandb")
    os.environ["WANDB_MODE"] = "online"
    os.environ["WANDB_API_KEY"] = "48454db87872b0da16c749491c7e362e5933ceee"
    user = "calisircihan21"
    project = "XPlane11"
    display_name = "Xplane11Training_A2C_1"
    wandb.init(entity=user, project=project, name=display_name)
    for episode in range(cfg.max_episode):
        state = env.reset()
        episode_score = 0
        start_time = time.perf_counter()

        for episode_steps in count():
            action = get_action(torch.tensor(state/np.max(state)).float()[None, :]).item()
            print("step: ", episode_steps, "action: ", action)
            next_state, reward, done, _ = env.step(action)

            memory.append([state, action, next_state, reward, done])
            state = next_state
            episode_score += reward

            if len(memory) > cfg.batch_size:
                states, actions, next_states, rewards, dones = \
                  map(lambda x: torch.tensor(x).float(), zip(*memory.sample_batch(cfg.batch_size)))

                # calculate estimated return
                targets = rewards + cfg.gamma * get_state_value(next_states).detach() * (1 - dones)
                td_errors = targets - get_state_value(states).detach()

                update_actor(states=states, actions=actions, advantages=td_errors)
                update_critic(states, targets)

            if done:
                last_scores.append(episode_score)
                print('episode: %d avg score %.5f, steps %d' % (episode, np.mean(last_scores[-100:]), episode_steps))
                wandb.log({"episode_reward": episode_score, "episode": episode})
                break

    env.close()


if __name__ == '__main__':
    main()
    plt.pause(0)