Y = []
name = []

N = int(input())

for i in range(N):
    a = input().split(" ")
    Y.append(int(a[0]))
    name.append(a[1])

for i in range(N):
    changed = False
    for j in range(N-1-i):
        if Y[j] > Y[j+1]:
            Y[j], Y[j+1] = Y[j+1], Y[j]
            name[j], name[j+1] = name[j+1], name[j]
        changed = True
        if not changed:
            break
for i in range(N):
    print(Y[i], name[i])
