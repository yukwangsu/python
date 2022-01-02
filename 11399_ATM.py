n = int(input())
a = input().split()
L = []
for i in range(n):
    L.append(int(a[i]))
L.sort()
total = 0
stack = 0
for i in range(n):
    stack += L[i]
    total += stack
print(total)