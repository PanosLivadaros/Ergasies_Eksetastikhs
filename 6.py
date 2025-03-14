import random


def placing(piece):
    a = random.randint(0, 7)
    b = random.randint(0, 7)
    while chessboard[a][b] != 0:
        a = random.randint(0, 7)
        b = random.randint(0, 7)
    chessboard[a][b] = piece


def index_2d(my_list, v):
    for i, x in enumerate(my_list):
        if v in x:
            return i, x.index(v)


def checking(x, y):
    global player1_points, player2_points
    if y:             # horizontal check
        for i in range(7):
            count = 0
            for j in range(7):
                if chessboard[i][j] == x or chessboard[i][j] == "black queen":
                    count += 1
                if count == 2:
                    if x == "white rook":
                        player1_points += 1
                    player2_points += 1
                    break
            else:
                continue
            break
    else:                   # vertical check
        for j in range(7):
            count = 0
            for i in range(7):
                if chessboard[i][j] == x or chessboard[i][j] == "black queen":
                    count += 1
                if count == 2:
                    if x == "white rook":
                        player1_points += 1
                    player2_points += 1
                    break
            else:
                continue
            break


player1_points = player2_points = 0
for z in range(100):
    chessboard = [[0] * 8 for j in range(8)]
    placing("white rook")
    placing("black queen")
    placing("white bishop")
    checking("white rook", True)
    checking("white rook", False)
    checking("white bishop", True)
    checking("white bishop", False)
    position = [[*index_2d(chessboard, "white rook")], [*index_2d(chessboard, "black queen")], [*index_2d(chessboard, "white bishop")]]
    if abs(position[0][0] - position[1][0]) == abs(position[0][1] - position[1][1]):        # diagonal check
        player2_points += 1
    elif abs(position[1][0] - position[2][0]) == abs(position[1][1] - position[2][1]):
        player1_points += 1
        player2_points += 1
print("After 100 games, player 1 has:", player1_points, "points and player 2 has:", player2_points, "points.")
