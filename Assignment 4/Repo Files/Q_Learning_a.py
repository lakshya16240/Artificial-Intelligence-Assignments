import numpy as np
import gym
import gym_maze
from collections import defaultdict
import matplotlib.pyplot as plt

env = gym.make('maze-sample-5x5-v0')

def to_25(a):
    x = a[0]
    y = a[1]
    row = x*5 + y
    return row 

def from_25(a):
    y = a%5
    x = a - y
    x /= 5
    x = int(x)
    return x,y


def to_words(action):
    if action == 0:
        action = "N"
    if action == 1:
        action = "E"
    if action == 2:
        action = "S"
    if action == 3:
        action = "W"
    return action

def choose_action(Q,observation):
    if np.equal.reduce(Q[observation]):
        return env.action_space.sample()
    else:
        return np.argmax(Q[observation])

def Q_Learning(alpha, episodes, epsilon, gamma ):
    
    Q = defaultdict(lambda: np.zeros(4))

    iterations = []

    for i in range(episodes):
        #first step 
        observation = env.reset()
        print(i)
        observation = to_25(observation)
        
        done = False
        iter = 0
        while not done:
            action = choose_action(Q,observation)
            # print(action)
            
            w_action = to_words(action)
            # print("action:",w_action)
            next_obs, reward, done,_= env.step(w_action)
            next_obs = to_25(next_obs)
            # if algo == "Q":
            Q[observation][action] += alpha*(reward + gamma* np.max(Q[next_obs]) - Q[observation][action])
            # elif algo == "S":
            #     new_action = eps_greedy(Q, next_obs, epsilon)
            #     Q[observation][action] += alpha*(reward + gamma* Q[next_obs][new_action] - Q[observation][action])
            
            observation = next_obs
            iter +=1
            env.render()
            if done == True:
                iterations.append(iter)
                break

    return iterations

iterations = Q_Learning(0.1,200,0.1, 0.4)
plt.plot(iterations)
plt.xlabel("No. of episodes")
plt.ylabel("Iterations")
plt.show()