import copy
import time


def game_over(state):
    if ((state[0][0] == 1 and state[0][1] == 1 and state[0][2] == 1) or (
            state[1][0] == 1 and state[1][1] == 1 and state[1][2] == 1) or
            (state[2][0] == 1 and state[2][1] == 1 and state[2][2] == 1) or (
                    state[0][0] == 1 and state[1][0] == 1 and state[2][0] == 1) or
            (state[0][1] == 1 and state[1][1] == 1 and state[2][1] == 1) or (
                    state[0][2] == 1 and state[1][2] == 1 and state[2][2] == 1) or
            (state[0][0] == 1 and state[1][1] == 1 and state[2][2] == 1) or (
                    state[0][2] == 1 and state[1][1] == 1 and state[2][0] == 1)):

        return 1

    elif ((state[0][0] == 0 and state[0][1] == 0 and state[0][2] == 0) or (
            state[1][0] == 0 and state[1][1] == 0 and state[1][2] == 0) or
          (state[2][0] == 0 and state[2][1] == 0 and state[2][2] == 0) or (
                  state[0][0] == 0 and state[1][0] == 0 and state[2][0] == 0) or
          (state[0][1] == 0 and state[1][1] == 0 and state[2][1] == 0) or (
                  state[0][2] == 0 and state[1][2] == 0 and state[2][2] == 0) or
          (state[0][0] == 0 and state[1][1] == 0 and state[2][2] == 0) or (
                  state[0][2] == 0 and state[1][1] == 0 and state[2][0] == 0)):

        return -1

    else:
        return 0



def move(state, player, x, flag):
    result = game_over(state)
    # print(result)
    # for i in range(3):
    #     for j in range(3):
    #         print(state[i][j], end=' ')
    #     print("\n")
    # print("\n")

    if (x == 9 or result == 1 or result == -1):
        return result

    else:
        if player == 1:
            value = -200
        else:
            value = 200

        best_move = [-1, -1]
        for i in range(3):
            for j in range(3):
                if state[i][j] == -1:
                    b = copy.deepcopy(state)
                    if player == 0:
                        b[i][j] = 0
                        returned_value = move(b, 1, x + 1, False)
                        if returned_value < value:
                            best_move = [i, j]
                            value = returned_value
                            # print("max value = " + str(value))
                    else:
                        b[i][j] = 1
                        returned_value = move(b, 0, x + 1, False)
                        if returned_value > value:
                            best_move = [i, j]
                            value = returned_value
                            # print("min value = " + str(value))

        if(flag):
            # print("move: ", best_move[0], best_move[1], player)
            b = copy.deepcopy(state)
            # print(player)
            if(player == 0):
                finState[best_move[0]][best_move[1]] = 0
                b[best_move[0]][best_move[1]] = 0
                move(b, 1, x + 1, True)
            else:
                finState[best_move[0]][best_move[1]] = 1
                b[best_move[0]][best_move[1]] = 1
                move(b, 0, x + 1, True)


        # if player == 1:
        #     print("here2 " + str(x))
        #     moves[best_move[0]][best_move[1]] = 1
        #     # for i in range(3):
        #     #     for j in range(3):
        #     #         print(moves[i][j],end = ' ')
        #     #     print("\n")
        #     # print("\n")
        # else:
        #     print("here " + str(x))
        #     moves[best_move[0]][best_move[1]] = 0
        #     # for i in range(3):
        #     #     for j in range(3):
        #     #         print(moves[i][j],end = ' ')
        #     #     print("\n")
        #     # print("\n")
        return value

start = time.time()
initial_state = []
finState = [[0 for i in range(3)] for j in range(3)]
moves = []
for i in range(3):
    initial_state.append([-1 for j in range(3)])

value = -200
for i in range(3):
    for j in range(3):
        print("NEXT")
        b = copy.deepcopy(initial_state)
        moves = copy.deepcopy(initial_state)
        b[i][j] = 1
        moves[i][j] = 1
        finState[i][j] = 1
        # print([i, j])
        returned_value = move(b, 0, 1, True)
        if (returned_value > value):
            best_move = [i, j]
            value = returned_value
        # value = max(value,move(b,0,1))
        for k in range(3):
            for l in range(3):
                print(finState[k][l], end=' ')
            print("\n")

end = time.time()
print("Time Taken " + str(end - start))