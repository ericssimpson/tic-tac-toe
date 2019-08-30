import random
import sys

print("Tic Tac Toe")
print("Board Set-Up")
print("0|1|2")
print("3|4|5")
print("6|7|8")
print("Enter Move: (HUMAN = O, AI = X)")

pairs = ([0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6])

corners = [0, 2, 6, 8]
board = ["_", "_", "_", "_", "_", "_", " ", " ", " "]

Turn = "PLAYER"
cpu_turn = 0

def printboard(Turn, board, cpu_turn):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("Turn: " + str(Turn))
    if Turn == 0:
        hum_move(Turn, board, cpu_turn)
    if Turn == "AI":
        cpu_turn += 1
        cpu_move(Turn, board, cpu_turn, corners)
    if Turn == "PLAYER":
        hum_move(Turn, board, cpu_turn)

def hum_move(Turn, board, cpu_turn):
    choice = input("Enter a number 0-8: ")
    if choice.isdigit() == False:
        print("Integer's Only")
        hum_move(Turn, board, cpu_turn)
    if int(choice) > 8 or int(choice) < 0:
        print("Number Between 0 and 8 Only")
        hum_move(Turn, board, cpu_turn)
    if board[int(choice)] == 'X' or board[int(choice)] == 'O':
        print("Spot Is Occupied")
        hum_move(Turn, board, cpu_turn)
    else:
        board[int(choice)] = "O"
    Turn = "AI"
    checkwin(Turn, board, cpu_turn)

def cpu_move(Turn, board, cpu_turn, corners):
    alreadymoved = False
    completes = ([0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6])

    def cornerchoice(corners, board, alreadymoved):
        goodchoices = []
        if not alreadymoved:
            for i in corners:
                if board[i] == " " or board[i] == "_":
                    goodchoices.append(i)
            board[random.choice(goodchoices)] = "X"

    if cpu_turn == 1:
        if board[4] != "O":
            board[4] = "X"
            alreadymoved = True
        else:
            cornerchoice(corners, board, alreadymoved)
            alreadymoved = True

    else:
        for x in completes:
            # Offensive
            if board[x[0]] == "X" and board[x[1]] == "X" and board[x[2]] != "O":
                board[x[2]] = "X"
                alreadymoved = True
                break
            if board[x[1]] == "X" and board[x[2]] == "X" and board[x[0]] != "O":
                board[x[0]] = "X"
                alreadymoved = True
                break
            if board[x[0]] == "X" and board[x[2]] == "X" and board[x[1]] != "O":
                board[x[1]] = "X"
                alreadymoved = True
                break

        for x in completes:
            if alreadymoved == False:
                # Defensive
                if board[x[0]] == "O" and board[x[1]] == "O" and board[x[2]] != "X":
                    board[x[2]] = "X"
                    alreadymoved = True
                    break
                if board[x[1]] == "O" and board[x[2]] == "O" and board[x[0]] != "X":
                    board[x[0]] = "X"
                    alreadymoved = True
                    break
                if board[x[0]] == "O" and board[x[2]] == "O" and board[x[1]] != "X":
                    board[x[1]] = "X"
                    alreadymoved = True
                    break

    if not alreadymoved:
        if cpu_turn == 2 and board[4] == "O":
            cornerchoice(corners, board, alreadymoved)
        else:
            sides = [1, 3, 5, 7]
            humansides = 0
            for i in sides:
                if board[i] == "O":
                    humansides += 1
            if humansides >= 1:
                cornerchoice(corners, board, alreadymoved)
            else:

                goodchoices = []
                for i in sides:
                    if board[i] == " " or board[i] == "_":
                        goodchoices.append(i)
                if goodchoices == []:
                    cornerchoice(corners, board, alreadymoved)
                else:
                    board[random.choice(goodchoices)] = "X"

    Turn = "PLAYER"
    checkwin(Turn, board, cpu_turn)


def checkwin(Turn, board, cpu_turn):
    for x in pairs:
        zero = board[x[0]]
        one = board[x[1]]
        two = board[x[2]]
        if zero == one and one == two:
            if zero == "X":
                print("AI wins.")
                end()
            if zero == "O":
                print("Human wins. Did you cheat?")
                end()
        else:
            filledspaces = 0
            for i in range(8):
                if board[i] != " " and board[i] != "_":
                    filledspaces += 1
                if filledspaces == 8:
                    print("A draw! You will never win!")
                    end()

    printboard(Turn, board, cpu_turn)

def end():
    print("Here is the final board.")
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    sys.exit(0)


printboard(Turn, board, cpu_turn)