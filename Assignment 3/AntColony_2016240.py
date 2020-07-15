from random import randint
import networkx
import numpy
from math import pow
from networkx import nx
from random import random
import matplotlib.pyplot as plt

# no. of ants = # cities


# alpha = 1
# beta = .4
no_of_cities = 10
no_of_ants = no_of_cities - 2
Q = 5000
evap = 0.5


class Ant:

    def __init__(self, city, visitedCitiesSet, distanceTravelled):
        self.currentCity = city
        self.visitedCitiesSet = visitedCitiesSet
        self.distanceTravelled = distanceTravelled


def calculateProbability(currentCity, destCity, visitedCities):
    dist = graph[currentCity][destCity]['weight']
    phero = pheromone[currentCity][destCity]
    sum = 0
    for i in range(no_of_cities):
        if i != currentCity and (i not in visitedCities):
            sum += pow(pheromone[currentCity][i], alpha) * pow(1 / graph[currentCity][i]['weight'], beta)

    if sum == 0:
        probability = 1 / (no_of_cities - visitedCities.__len__())
    else:
        probability = (pow(phero, alpha) * pow(1 / dist, beta)) / sum

    return probability


def moveAnt(ant):
    currentCity = ant.currentCity
    visitedCities = ant.visitedCitiesSet
    probability = [0 for i in range(no_of_cities)]
    for i in range(no_of_cities):
        if i != currentCity and (i not in visitedCities):
            probability[i] = calculateProbability(currentCity, i, visitedCities)

    x = random()
    y = 0
    destCity = -1
    # print(probability, x)
    for i in range(no_of_cities):
        # print(y)
        if not y <= x < (y + probability[i]):
            y += probability[i]

        else:
            destCity = i
            break

    ant.distanceTravelled += graph[currentCity][destCity]['weight']
    # print("probability ", probability)
    return destCity


def updatePheromone(ant, distanceTravelled):
    visitedCities = ant.visitedCitiesSet
    pheromoneToBeDeposited = Q / distanceTravelled

    city = visitedCities.pop()
    pheromone[city][visitedCities[0]] = (1 - evap) * pheromone[city][visitedCities[0]] + pheromoneToBeDeposited
    pheromone[visitedCities[0]][city] = (1 - evap) * pheromone[city][visitedCities[0]] + pheromoneToBeDeposited

    startCity = city

    while visitedCities.__len__() != 1:
        city = visitedCities.pop()
        pheromone[startCity][city] = (1 - evap) * pheromone[city][visitedCities[0]] + pheromoneToBeDeposited
        pheromone[city][startCity] = (1 - evap) * pheromone[city][visitedCities[0]] + pheromoneToBeDeposited
        startCity = city

    pheromone[startCity][visitedCities[0]] = (1 - evap) * pheromone[city][visitedCities[0]] + pheromoneToBeDeposited
    pheromone[visitedCities[0]][startCity] = (1 - evap) * pheromone[city][visitedCities[0]] + pheromoneToBeDeposited


##############################################################

distances = [[0 for i in range(no_of_cities)] for j in range(no_of_cities)]
pheromone = [[0 for i in range(no_of_cities)] for j in range(no_of_cities)]
ants = [Ant(randint(0, no_of_cities - 1), [], 0) for i in range(no_of_ants)]

for i in range(no_of_cities):
    for j in range(no_of_cities):
        if i != j and distances[i][j] == 0:
            distances[i][j] = randint(1, 20)
            distances[j][i] = distances[i][j]

# plot graph

graph = networkx.from_numpy_matrix(numpy.array(distances))
print(distances)
pos = nx.shell_layout(graph)
nx.draw_networkx_nodes(graph, pos, node_size=80)
nx.draw_networkx_labels(graph, pos, font_size=13, font_family='sans-serif')
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, label_pos=0.61)

nx.draw(graph, pos)
plt.axis('off')
plt.show()
print()

# assign ants to cities

for i in range(no_of_ants):
    ants[i].visitedCitiesSet.append(ants[i].currentCity)

# start process

alphaBeta = [[0.5, 1.2], [2, 0.4], [1, 4], [1, 1]]

d = 0
while d < 4:
    a = alphaBeta[d]
    alpha = a[0]
    beta = a[1]
    count = 0
    while count < 500:
        for i in range(no_of_ants):
            # print("ant : ", i)
            while ants[i].visitedCitiesSet.__len__() != no_of_cities:
                destCity = moveAnt(ants[i])
                ants[i].currentCity = destCity
                ants[i].visitedCitiesSet.append(destCity)

        for i in range(no_of_ants):
            distance = ants[i].distanceTravelled
            updatePheromone(ants[i], distance)
            ants[i].currentCity = ants[i].visitedCitiesSet[0]

        count += 1

    print("pheromone levels : ")
    for i in range(no_of_cities):
        for j in range(no_of_cities):
            print(pheromone[i][j], end="    ")
        print()
    print()

    print("best path : ")

    c = 0
    city = 0
    v = [city]
    distance = 0
    index = -1
    while c < 5:
        max = 0
        index = -1
        for i in range(no_of_cities):
            if i not in v and pheromone[city][i] > max:
                max = pheromone[city][i]
                index = i
        print(city, " to ", index)
        distance += distances[city][index]
        city = index
        v.append(city)
        c += 1

    print(index, " to ", v[0])
    print("total distance travelled = ", distance)

    d+=1
