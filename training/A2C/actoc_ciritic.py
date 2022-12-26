import torch.nn as nn
import torch.nn.init as init
import torch.nn.functional as F

class Actor(nn.Module):
  def __init__(self, env):
    super(Actor, self).__init__()
    self.state_dim = env.observation_space.shape[0]
    self.action_dim = env.action_space[0].n
    self.fc1 = nn.Linear(self.state_dim, 32)
    self.fc2 = nn.Linear(32, self.action_dim)
    init.xavier_normal_(self.fc1.weight)
    init.xavier_normal_(self.fc2.weight)

  def forward(self, x):
    x = F.elu(self.fc1(x))
    x = F.softmax(self.fc2(x), dim=1)
    return x


class Critic(nn.Module):
  def __init__(self, env):
    super(Critic, self).__init__()
    self.state_dim = env.observation_space.shape[0]
    self.fc1 = nn.Linear(self.state_dim, 64)
    self.fc2 = nn.Linear(64, 1)
    init.xavier_normal_(self.fc1.weight)

  def forward(self, x):
    x = F.elu(self.fc1(x))
    value = self.fc2(x)
    return value.squeeze()