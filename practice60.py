a = input().split(" ")
N = int(a[0])
M = int(a[1])
b = input().split(" ")
num =[]
for i in range(N):
    num.append(int(b[i]))
for i in range(N):
    num[i] = num[i] % M
c =[0 for _ in range(M)]
for i in range(N):
    c[num[i]] += 1
max = 0
for i in c:
    if i > max:
        max = i
maxmax = []
for i in range(M):
    d = 0
    for j in range(N):
        if i == num[j]:
            d += 1
    if d == max:
        maxmax.append(i)   
print("{0}개 : {1}".format(max, maxmax))
for i in range(M):
    if c[i] == max:
        c[i] = 0
max = 0
for i in c:
    if i > max:
        max = i
if max != 0:
    maxmax = []
    for i in range(M):
        d = 0
        for j in range(N):
            if i == num[j]:
                d += 1
        if d == max:
            maxmax.append(i)
    print("{0}개 : {1}".format(max, maxmax))
