import sys 
a = sys.stdin.readline().rstrip().split()
n = int(a[0])
m = int(a[1])
t_move = m
back_list = []
for i in range(n):
    move = sys.stdin.readline().rstrip().split()
    start = int(move[0])
    finish = int(move[1])
    long = start - finish
    direc = (long < 0)
    if not direc:
        back_list.append([finish, start])
back_list.sort()
t_min = back_list[0][0]
t_max = back_list[0][1]
gap = 0
for i in range(len(back_list)):
    if back_list[i][0] > t_max:
            gap += back_list[i][0] - t_max
    if back_list[i][1] > t_max:
        t_max = back_list[i][1]
    
t_move += 2*(t_max-t_min-gap)
print(round(t_move)) 