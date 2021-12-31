n = int(input())
a = []
for i in range(n):
    b = input().split()
    a.append([int(b[0]), int(b[1])])
a.sort()
time = a[0][0] + a[0][1]
for k in range(1, n):
    if a[k][0] > time:
        time = a[k][0]
        time += a[k][1]
    else:
        time += a[k][1]
print(time)