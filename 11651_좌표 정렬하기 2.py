import sys
n = int(input())
a = []
for i in range(n):
    b = sys.stdin.readline().rstrip().split()
    a.append([int(b[1]), int(b[0])])
a.sort()
for i in range(n):
    print(a[i][1], a[i][0])