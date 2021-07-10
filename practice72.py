a = input().split(" ")
b = []
for i in range(len(a)):
    b.append(a[i])
for i in range(len(b)):    
    b[i] = len(b[i])
m = 0
for i in range(len(b)):
    if m < b[i]:
        m = b[i]
n = int(m)
for k in range(m):
    for i in range(len(b)):
        if b[i] >= n:
            print("*", end = "")
        else:
            print(" ", end = "")
    n -= 1
    print()