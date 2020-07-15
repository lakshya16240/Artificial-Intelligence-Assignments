import numpy as np
import gym
import gym_maze
from collections import defaultdict
import matplotlib.pyplot as plt
import random

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

def choose_action(Q,observation,episode_number,epsilon):
    
    if random.random() <=epsilon:
        return np.argmax(Q[observation])
    else:
        p = calculate_probability(Q,observation,episode_number)
        x = random.random()
        print("p",p)
        if 0<= x <= p[0]:
            return 0
        elif p[0]< x <= p[0] + p[1]:
            return 1
        elif p[1]< x <=p[0] + p[1] + p[2]:
            return 2
        else :
            return 3

def calculate_probability(Q,observation,episode_number):
    p =[0,0,0,0]
    sum = 0
    for i in range(4):
        sum += abs(Q[observation][i])
    
    if sum != 0 or episode_number != 0:
        for i in range(4):
            p[i] = abs(Q[observation][i])/sum
        return p
    else:
        p = [0.25,0.25,0.25,0.25]
        return p



def Q_Learning(alpha, episodes, epsilon, gamma):
    
    Q = defaultdict(lambda: np.zeros(4))
    # Q = np.zeros((25,4), dtype = 'int32')
    probability_values = []
    for i in range(episodes):
        #first step 
        observation = env.reset()
        observation = to_25(observation)
        done = False
        while not done:
            action = choose_action(Q,observation,i,epsilon)
        
            w_action = to_words(action)
            # print("action:",w_action)
            next_obs, reward, done,_= env.step(w_action)
            next_obs = to_25(next_obs)
            Q[observation][action] += alpha*(reward + gamma* np.max(Q[next_obs]) - Q[observation][action])
        
            # print(Q)
            observation = next_obs
            # env.render()
            if done == True:
                p=calculate_probability(Q,17,i)
                probability_values.append(p)
    return probability_values

probability_values = Q_Learning(0.1,200, 0.2, 0.4)
plt.plot(probability_values)
plt.xlabel("No. of episodes")
plt.ylabel("Probability")
plt.legend(["Upward", "Rightward","Leftward","Downward"],loc = "right")
plt.show()


