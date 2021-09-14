from collections import deque
a = input().split(" ")
n = int(a[0])
m = int(a[1])
die_list = deque()
live_list = deque()
for i in range(n):
    live_list.append(int(i+1))
for i in range(n):
    die = 0
    stack = 1
    while die == 0:
        if stack != m:
            live_list.append(live_list[0])
            live_list.popleft()
            stack += 1
        else:
            die_list.append(live_list[0])
            live_list.popleft()
            die = 1
print("<", end = "")
for i in range(n-1):
    print(die_list[i], end = ", ")
print(die_list[n-1], end = "")
print(">")