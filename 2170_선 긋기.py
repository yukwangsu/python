import sys
n = int(input())
a = []
t_max = -10**15
t_min = 10**15
for i in range(n):
    b = sys.stdin.readline().rstrip().split()
    a.append([int(b[0]),int(b[1])])
    if a[i][1] > t_max:
        t_max = a[i][1]
    if a[i][0] < t_min:
        t_min = a[i][0]
a.sort()
gap = 0
max = a[0][1]
for i in range(1,n):
    if a[i][0] > max:
        gap += a[i][0]-max
    if a[i][1] > max:
        max = a[i][1]    
print(t_max-t_min-gap)