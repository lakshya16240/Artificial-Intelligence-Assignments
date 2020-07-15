from random import randint
import copy
import time
from math import ceil
from queue import PriorityQueue


class Node:
    next_right = None
    next_left = None
    next_up = None
    next_down = None
    color = None

    def __init__(self, color=None):
        self.color = color


class Configuration:

    def __init__(self, matrix, name, steps, components):
        self.matrix = matrix
        self.name = name
        self.steps = steps
        self.components = components

    def __lt__(self, other):
        return self.components >= other.components


def computeString(matrix):
    name = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            name = name + str(matrix[i][j])

    return name


def isExisting(name):
    var = name in processed
    # print(str(var) + " " + name)
    return var


def validation(a):
    b = [0,0,0,0]
    for i in range(len(a)):
        for j in range(len(a[0])):
            b[a[i][j] - 1] +=1

    for i in range(4):
        x = b[i]
        if x> ceil(len(a)*len(a) / 2) :
            return False

    return True



def process(config):
    # print("processing")
    matrix = config[1].matrix
    print(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # if i != len(matrix) - 1 and matrix[i][j] == matrix[i + 1][j]:
            #
            # if i != 0 and matrix[i][j] == matrix[i - 1][j]:
            #
            # if j != 0 and matrix[i][j] == matrix[i][j - 1]:
            #
            # if j != len(matrix[0]) - 1 and matrix[i][j] == matrix[i][j + 1]:
            # print("entering")
            if (i != len(matrix) - 1 and matrix[i][j] == matrix[i + 1][j]) or (
                    i != 0 and matrix[i][j] == matrix[i - 1][j]) or (j != 0 and matrix[i][j] == matrix[i][j - 1]) or (
                    j != len(matrix[0]) - 1 and matrix[i][j] == matrix[i][j + 1]):

                if i != len(matrix) - 1 and matrix[i][j] != matrix[i + 1][j]:
                    b = copy.deepcopy(matrix)
                    # print("condition1")
                    x = b[i][j]
                    b[i][j] = b[i + 1][j]
                    b[i + 1][j] = x
                    name = computeString(b)
                    components = connected_components(b)
                    # print(components)
                    if components == len(matrix)*len(matrix):
                        print("solved1")
                        print(str(b) + " " + str(config[1].steps + 1))
                        return True
                    test = isExisting(name)
                    if not test:
                        process_space.put((total - components + config[1].steps + 1, Configuration(b, name, config[1].steps + 1, components)))
                        processed.add(name)

                if i != 0 and matrix[i][j] != matrix[i - 1][j]:
                    b = copy.deepcopy(matrix)
                    # print("condition2")
                    x = b[i][j]
                    b[i][j] = b[i - 1][j]
                    b[i - 1][j] = x
                    name = computeString(b)
                    components = connected_components(b)
                    # print(components)
                    if components == len(matrix)*len(matrix):
                        print("solved1")
                        print(str(b) + " " + str(config[1].steps + 1))
                        return True
                    test = isExisting(name)
                    if not test:
                        process_space.put((total - components + config[1].steps + 1, Configuration(b, name, config[1].steps + 1, components)))
                        processed.add(name)

                if j != 0 and matrix[i][j] != matrix[i][j - 1]:
                    b = copy.deepcopy(matrix)
                    # print("condition3")
                    x = b[i][j]
                    b[i][j] = b[i][j - 1]
                    b[i][j - 1] = x
                    name = computeString(b)
                    components = connected_components(b)
                    # print(components)
                    if components == len(matrix)*len(matrix):
                        print("solved1")
                        print(str(b) + " " + str(config[1].steps + 1))
                        return True
                    test = isExisting(name)
                    if not test:
                        process_space.put((total - components + config[1].steps + 1, Configuration(b, name, config[1].steps + 1, components)))
                        processed.add(name)

                if j != len(matrix[0]) - 1 and matrix[i][j] != matrix[i][j + 1]:
                    b = copy.deepcopy(matrix)
                    # print("condition4")
                    x = b[i][j]
                    b[i][j] = b[i][j + 1]
                    b[i][j + 1] = x
                    name = computeString(b)
                    components = connected_components(b)
                    # print(components)
                    if components == len(matrix)*len(matrix):
                        print("solved1")
                        print(str(b) + " " + str(config[1].steps + 1))
                        return True
                    test = isExisting(name)
                    if not test:
                        process_space.put((total - components + config[1].steps + 1, Configuration(b, name, config[1].steps + 1, components)))
                        processed.add(name)


def dfs(i, j, b,visited):
    visited[i][j] = True
    if b[i][j].next_right is not None and not visited[i][j + 1]:
        dfs(i, j + 1, b,visited)
    if b[i][j].next_left is not None and not visited[i][j - 1]:
        dfs(i, j - 1, b,visited)
    if b[i][j].next_down is not None and not visited[i + 1][j]:
        dfs(i + 1, j, b,visited)
    if b[i][j].next_up is not None and not visited[i - 1][j]:
        dfs(i - 1, j, b,visited)


def connected_components(a):
    # print("solving : " + str(a))
    b = [[Node() for x in range(len(a))] for y in range(len(a[0]))]
    visited = [[False for k in range(len(a[0]))] for l in range(len(a))]
    count = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            b[i][j] = Node(a[i][j])

    for i in range(len(a)):
        for j in range(len(a[0])):
            if i != len(a) - 1 and a[i][j] == a[i + 1][j]:
                b[i][j].next_down = b[i + 1][j]
            if i != 0 and a[i][j] == a[i - 1][j]:
                b[i][j].next_up = b[i - 1][j]
            if j != 0 and a[i][j] == a[i][j - 1]:
                b[i][j].next_left = b[i][j - 1]
            if j != len(a[0]) - 1 and a[i][j] == a[i][j + 1]:
                b[i][j].next_right = b[i][j + 1]

    for i in range(len(a)):
        for j in range(len(a[0])):
            if not visited[i][j]:
                dfs(i, j, b,visited)
                count += 1

    return count


# n = int(input())
process_space = PriorityQueue()
processed = set()
boolean = False
count = 0
# a = [[0 for i in range(n)] for j in range(n)]
a = [[1, 1, 3, 1, 1], [4, 3, 3, 1, 3], [1, 3, 2, 2, 3], [3, 1, 4, 3, 4], [4, 3, 1, 2, 2]]


# for i in range(n):
#     for j in range(n):
#         a[i][j] = randint(1, 4)

total = len(a)*len(a)
print(a)

start = time.time()

vali = validation(a)
if not vali:
    print("Cannot be solved")
else:
    name = computeString(a)
    components = connected_components(a)
    process_space.put((total - components,Configuration(a, name,0,components)))
    processed.add(name)

    while not process_space.empty():
        config = process_space._get()
        components = connected_components(config[1].matrix)
        count = count + 1

        # print(components)
        if components == len(a) * len(a):
            print("Solved!")
            break
        boolean = process(config)
        if boolean:
            break
end = time.time()
print("no. of nodes explored : " + str(count))
print("Time taken : " + str(end - start))
