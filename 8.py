import random

def placing(piece, m, n):
    a = random.randint(0, m-1)
    b = random.randint(0, n-1)
    while chessboard[a][b] != 0:
        a = random.randint(0, m-1)
        b = random.randint(0, n-1)
    chessboard[a][b] = piece

def index_2d(my_list, v):
    for i, x in enumerate(my_list):
        if v in x:
            return i, x.index(v)

def checking(x, y, k, l):
    global player1_points, player2_points
    if y:             # horizontal check
        for i in range(k-1):
            count = 0
            for j in range(l-1):
                if chessboard[i][j] == x or chessboard[i][j] == "white rook":
                    count += 1
                if count == 2:
                    player1_points += 1
                    break
            else:
                continue
            break
    else:                   # vertical check
        for j in range(l-1):
            count = 0
            for i in range(k-1):
                if chessboard[i][j] == x or chessboard[i][j] == "white rook":
                    count += 1
                if count == 2:
                    player1_points += 1
                    break
            else:
                continue
            break

def base(m, n):
    global chessboard, player1_points, player2_points
    player1_points = 0
    player2_points = 0
    for z in range(100):
        chessboard = [[0] * n for f in range(m)]
        placing("white rook", m, n)
        placing("black bishop", m, n)
        checking("black bishop", True, m, n)
        checking("black bishop", False, m, n)
        position = [[*index_2d(chessboard, "white rook")], [*index_2d(chessboard, "black bishop")]]
        if abs(position[0][0] - position[1][0]) == abs(position[0][1] - position[1][1]):  # diagonal check
            player2_points += 1
    print("For game with chessboard size: ", m, "x", n, ": \nAfter 100 games, player 1 has:", player1_points, "points and player 2 has:", player2_points, "points.")

chessboard=[]
player1_points = player2_points = 0
base(8, 8)
base(7, 8)
base(7, 7)
