import queue
import copy
import time

process_space = queue.Queue()
processed = set()
final_value = "123456780"


class Node:

    def __init__(self, b, i, j, name,steps):
        self.arr = b
        self.index_row = i
        self.index_column = j
        self.name = name
        self.steps = steps


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
        # if len(a) > 1:
        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i + 1][j]
        b[i + 1][j] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i + 1, j, name,a.steps + 1))

        # if len(a[0]) > 1:
        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j+1]
        b[i][j+1] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i , j+1, name,a.steps + 1))


    elif i == 0 and j == len(a.arr[0]) - 1:

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i + 1][j]
        b[i + 1][j] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i + 1, j, name,a.steps + 1))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j - 1]
        b[i][j - 1] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i, j - 1, name,a.steps + 1))


    elif i == len(a.arr)-1 and j == len(a.arr[0]) - 1:


        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i - 1][j]
        b[i - 1][j] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i - 1, j, name,a.steps + 1))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j - 1]
        b[i][j - 1] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i, j - 1, name,a.steps + 1))


    elif i == len(a.arr)-1 and j == 0:

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i - 1][j]
        b[i - 1][j] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i - 1, j, name,a.steps + 1))


        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j + 1]
        b[i][j + 1] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i, j + 1, name,a.steps + 1))

    elif (i == 0 and j !=0) and (i == 0 and j != len(a.arr[0]) - 1):

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i + 1][j]
        b[i + 1][j] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i + 1, j, name,a.steps + 1))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j + 1]
        b[i][j + 1] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i, j + 1, name,a.steps + 1))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j - 1]
        b[i][j - 1] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i, j - 1, name,a.steps + 1))


    elif (i == len(a.arr)-1 and j !=0) and (i == len(a.arr)-1 and j != len(a.arr[0]) - 1):

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i - 1][j]
        b[i - 1][j] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i - 1, j, name,a.steps + 1))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j + 1]
        b[i][j + 1] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i, j + 1, name,a.steps + 1))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j - 1]
        b[i][j - 1] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i, j - 1, name,a.steps + 1))


    elif (j == len(a.arr)-1 and i !=0) and (j == len(a.arr)-1 and i != len(a.arr[0]) - 1):

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i - 1][j]
        b[i - 1][j] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i - 1, j, name,a.steps + 1))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j - 1]
        b[i][j - 1] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i, j - 1, name,a.steps + 1))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i+1][j]
        b[i+1][j] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i + 1, j, name,a.steps + 1))


    elif (j == 0 and i !=0) and (j == 0 and i != len(a.arr[0]) - 1):

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i - 1][j]
        b[i - 1][j] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i - 1, j, name,a.steps + 1))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j + 1]
        b[i][j + 1] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i, j + 1, name,a.steps + 1))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i+1][j]
        b[i+1][j] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i+1, j, name,a.steps + 1))


    elif (0 < i < len(a.arr)) and (0 < j < len(a.arr[0])):

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i + 1][j]
        b[i + 1][j] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i + 1, j, name,a.steps + 1))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i - 1][j]
        b[i - 1][j] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i - 1, j, name,a.steps + 1))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j + 1]
        b[i][j + 1] = x
        name = computeString(b)
        if name == final_value :
            print("solved : " + str(name))
            print("number of steps for solution" + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i, j + 1, name,a.steps + 1))

        b = copy.deepcopy(a.arr)
        x = b[i][j]
        b[i][j] = b[i][j - 1]
        b[i][j - 1] = x
        name = computeString(b)
        if name == final_value:
            print("solved : " + str(name))
            print("number of steps for solution : " + str(a.steps + 1))
            return True
        test = isExisting(name)
        if not test:
            process_space.put(Node(b, i, j - 1, name,a.steps + 1))



print("input value greater than or equal to 2")
n = int(input())
a = []
for i in range(n):
    a.append([0 for j in range(n)])
index_row = -1
index_column = -1
count = 0
boolean = False

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

matrix = Node(a, index_row, index_column,computeString(a),0)

process_space.put(matrix)

while process_space._qsize() > 0 :
    node = process_space._get()
    processed.add(node.name)
    count = count + 1
    boolean = process(node)
    if boolean:
        print("number of nodes explored : " + str(count))
        break
    

end = time.time()
print("time : " + str(end - start))


# if __name__ == "main":
#     print ("hello")
#     n = int(input())
#     a = []
#     for i in range(n):
#         a.append([0 for j in range(n)])
#     index_row = -1
#     index_column = -1
#     for i in range(n):
#         for j in range(n):
#             a[i][j] = int(input())
#             if a[i][j] == 0:
#                 index_row = i
#                 index_column = j
#
#     matrix = Node(a, index_row, index_column,computeString(a))
#     processed.add(computeString(matrix))
#     process_space.put(matrix)
#     process(0)
