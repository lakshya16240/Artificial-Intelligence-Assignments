import numpy as np
import gym
import gym_maze
from collections import defaultdict
import matplotlib.pyplot as plt

env = gym.make('maze-sample-5x5-v0')

def eps_greedy(Q,state,epsilon):
    if np.random.random_sample() >= epsilon:
        return np.argmax(Q[state])
    else:
        return np.random.randint(0, 4)

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

def Q_Learning(algo, alpha, episodes, epsilon, gamma ):
    #algo : Q for Q learning
    #S for Sarsa
    
    Q = defaultdict(lambda: np.zeros(4))
    iterations = []
    count = 0
    for i in range(episodes):
        observation = env.reset()
        print(i)
        observation = to_25(observation)
        
        iter = 0
        done = False
        
        while not done:
            action = eps_greedy(Q, observation, epsilon)
            w_action = to_words(action)
            next_obs, reward, done,_= env.step(w_action)
            next_obs = to_25(next_obs)
            if algo == "Q":
                Q[observation][action] += alpha*(reward + gamma* np.max(Q[next_obs]) - Q[observation][action])
            elif algo == "S":
                new_action = eps_greedy(Q, next_obs, epsilon)
                Q[observation][action] += alpha*(reward + gamma* Q[next_obs][new_action] - Q[observation][action])
            
            observation = next_obs
            iter += 1
            env.render()
            if done == True:
                if iter <=50:
                    count += 1
                else:
                    count = 0
                iterations.append(iter)

                break
    return iterations,count, Q


def run_different_maze(Q_table, alpha, episodes, epsilon, gamma):
    env = gym.make('maze-random-5x5-v0')
    Q = Q_table
    iterations = []
    count = 0
    for i in range(episodes):
        observation = env.reset()
        print(i)
        observation = to_25(observation)
        
        iter = 0
        done = False
        
        while not done:
            # action = eps_greedy(Q, observation, epsilon)
            action = np.argmax(Q[observation])
            w_action = to_words(action)
            next_obs, reward, done,_= env.step(w_action)
            next_obs = to_25(next_obs)
            # Q[observation][action] += alpha*(reward + gamma* np.max(Q[next_obs]) - Q[observation][action])
            
            observation = next_obs
            iter += 1
            env.render()
            if done == True:
                if iter <=50:
                    count += 1
                else:
                    count = 0
                iterations.append(iter)
                break


iterations, count, Q_table = Q_Learning("S",1,200,0.1,0.8)
plt.plot(iterations)
plt.xlabel("No. of episodes")
plt.ylabel("Iterations")
plt.show()

# run_different_maze(Q_table,1,200,0.1,0.8)

print("count",count)