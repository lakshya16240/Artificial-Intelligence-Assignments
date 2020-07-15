import copy
import math
import time
from queue import PriorityQueue

process_space = PriorityQueue()
processed = set()
final_value = "123456780"


class Node:

    def __init__(self, b, i, j, name, steps, distance):
        self.arr = b
        self.index_row = i
        self.index_column = j
        self.name = name
        self.steps = steps
        self.distance = distance

    def __lt__(self, other):
        return self.distance <= other.distance


def computeManhattanDistance(arr):
    dist = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != 0:
                row = int(arr[i][j] / len(arr))
                col = (arr[i][j] % len(arr)) - 1
                dist = dist + abs(row - i) + abs(col - j)

    # print(dist)
    return dist


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


def process(a):
    print(a.name)

    i = a.index_row
    j = a.index_column
    if i == 0 and j == 0:
        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i + 1][j]
        b[i + 1][j] = x
        name = computeString(b)
        if name == final_value:
            print(name)
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i + 1, j, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j + 1]
        b[i][j + 1] = x
        name = computeString(b)
        if name == final_value:
            print(name)
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i, j + 1, name, a.steps + 1, distance)))


    elif i == 0 and j == len(a.arr[0]) - 1:

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i + 1][j]
        b[i + 1][j] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i + 1, j, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j - 1]
        b[i][j - 1] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i, j - 1, name, a.steps + 1, distance)))


    elif i == len(a.arr) - 1 and j == len(a.arr[0]) - 1:

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i - 1][j]
        b[i - 1][j] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i - 1, j, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j - 1]
        b[i][j - 1] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i, j - 1, name, a.steps + 1, distance)))


    elif i == len(a.arr) - 1 and j == 0:

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i - 1][j]
        b[i - 1][j] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i - 1, j, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j + 1]
        b[i][j + 1] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i, j + 1, name, a.steps + 1, distance)))

    elif (i == 0 and j != 0) and (i == 0 and j != len(a.arr[0]) - 1):

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i + 1][j]
        b[i + 1][j] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i + 1, j, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j + 1]
        b[i][j + 1] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i, j + 1, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j - 1]
        b[i][j - 1] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i, j - 1, name, a.steps + 1, distance)))


    elif (i == len(a.arr) - 1 and j != 0) and (i == len(a.arr) - 1 and j != len(a.arr[0]) - 1):

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i - 1][j]
        b[i - 1][j] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i - 1, j, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j + 1]
        b[i][j + 1] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i, j + 1, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j - 1]
        b[i][j - 1] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i, j - 1, name, a.steps + 1, distance)))


    elif (j == len(a.arr) - 1 and i != 0) and (j == len(a.arr) - 1 and i != len(a.arr[0]) - 1):

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i - 1][j]
        b[i - 1][j] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i - 1, j, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j - 1]
        b[i][j - 1] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i, j - 1, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i + 1][j]
        b[i + 1][j] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i + 1, j, name, a.steps + 1, distance)))


    elif (j == 0 and i != 0) and (j == 0 and i != len(a.arr[0]) - 1):

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i - 1][j]
        b[i - 1][j] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i - 1, j, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j + 1]
        b[i][j + 1] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i, j + 1, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i + 1][j]
        b[i + 1][j] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i + 1, j, name, a.steps + 1, distance)))


    elif (0 < i < len(a.arr)) and (0 < j < len(a.arr[0])):

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i + 1][j]
        b[i + 1][j] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i + 1, j, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i - 1][j]
        b[i - 1][j] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i - 1, j, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j + 1]
        b[i][j + 1] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i, j + 1, name, a.steps + 1, distance)))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j - 1]
        b[i][j - 1] = x
        name = computeString(b)
        if name == final_value:
            print(name)
            return True
        test = isExisting(name)
        if not test:
            distance = computeManhattanDistance(b)
            process_space.put((distance + a.steps + 1, Node(b, i, j - 1, name, a.steps + 1, distance)))



print("input value greater than or equal to 2")
n = int(input())
a = []
flag = 0
for i in range(n):
    a.append([0 for j in range(n)])
index_row = -1
index_column = -1

final_matrix = []
temp = []

for i in range(1, n * n):

    temp.append(i)
    if i % n == 0:
        final_matrix.append(temp)
        temp = []
temp.append(0)
final_matrix.append(temp)

# for i in range(1,n*n):
#     final_value = final_value + str(i)
# final_value = final_value + "0"

for i in range(n):
    for j in range(n):
        a[i][j] = int(input())
        if a[i][j] == 0:
            index_row = i
            index_column = j

start = time.time()
distance = computeManhattanDistance(a)

matrix = Node(a, index_row, index_column, computeString(a), 0, distance)
process_space.put((matrix.distance, matrix))
processed.add(computeString(matrix.arr))
count = 0
boolean = False
while not process_space.empty():
    node = process_space.get()
    processed.add(node[1].name)
    # print("hello" + str(node[0]))
    count = count + 1
    # print("count : " + str(count))
    boolean = process(node[1])
    if count == math.factorial(n * n):
        flag = 1
    if boolean :
        break

if flag == 1:
    print("answer doesnt exist1")
elif not boolean:
    print("answer doesnt exist2")
else:
    print("number of nodes explored " + str(count))

end = time.time()
print("time : " + str(end - start))
