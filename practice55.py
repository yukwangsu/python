N = int(input())
list = []
for i in range(N):
    a = int(input())
    list.append(a)
m = 0
for i in range(N):
    if list[i] > m:
        m = list[i]
arr = [0 for _ in range(m+1)]
for i  in range(N):
    arr[list[i]] +=1

for i in range(m+1):
    if arr[i] > 0:
        print("{0}: {1}".format(i, arr[i]))