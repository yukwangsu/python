a = input().split(" ")
N = int(a[0])
M = int(a[1])
X = int(a[2])
Y = int(a[3])
K = int(a[4])
map = []
for i in range(N):
    b = input().split(" ")
    for j in range(M):
        map.append(int(b[j]))
move = []
c = input().split(" ")
for i in range(K):
    move.append(int(c[i]))
move_point_X = X
move_point_Y = Y
dice1 = [0 for _ in range(4)]
dice2 = [0 for _ in range(4)]
for i in range(K):
    if move[i] == 1:
        move_point_Y += 1
        if move_point_Y > M-1:
            move_point_Y -= 1
        else: 
            d = dice1[3]
            dice1.pop(3)
            dice1.insert(0,d)
            if map[M*move_point_X + move_point_Y] > 0:
                dice1[2] = map[M*move_point_X + move_point_Y]
                map[M*move_point_X + move_point_Y] = 0
                dice2[0], dice2[2] = dice1[0], dice1[2]
                print(dice1[0])
            else:
                map[M*move_point_X + move_point_Y] = dice1[2]
                dice2[0], dice2[2] = dice1[0], dice1[2]
                print(dice1[0])
    elif move[i] == 2:
        move_point_Y -= 1
        if move_point_Y < 0:
            move_point_Y += 1
        else:
            d = dice1[0]
            dice1.pop(0)
            dice1.insert(3,d)
            if map[M*move_point_X + move_point_Y] > 0:
                dice1[2] = map[M*move_point_X + move_point_Y]
                map[M*move_point_X + move_point_Y] = 0
                dice2[0], dice2[2] = dice1[0], dice1[2]
                print(dice1[0])
            else:
                map[M*move_point_X + move_point_Y] = dice1[2]
                dice2[0], dice2[2] = dice1[0], dice1[2]
                print(dice1[0])
    elif move[i] == 3:
        move_point_X -= 1
        if move_point_X < 0:
            move_point_X += 1
        else:
            d = dice2[0]
            dice2.pop(0)
            dice2.insert(3,d)
            if map[M*move_point_X + move_point_Y] > 0:
                dice2[2] = map[M*move_point_X + move_point_Y]
                map[M*move_point_X + move_point_Y] = 0
                dice1[0], dice1[2] = dice2[0], dice2[2]
                print(dice2[0])
            else:
                map[M*move_point_X + move_point_Y] = dice2[2]
                dice1[0], dice1[2] = dice2[0], dice2[2]
                print(dice2[0])
    elif move[i] == 4:
        move_point_X += 1
        if move_point_X > N-1:
            move_point_X -= 1
        else:
            d = dice2[3]
            dice2.pop(3)
            dice2.insert(0,d)
            if map[M*move_point_X + move_point_Y] > 0:
                dice2[2] = map[M*move_point_X + move_point_Y]
                map[M*move_point_X + move_point_Y] = 0
                dice1[0], dice1[2] = dice2[0], dice2[2]
                print(dice2[0])
            else:
                map[M*move_point_X + move_point_Y] = dice2[2]
                dice1[0], dice1[2] = dice2[0], dice2[2]
                print(dice2[0])