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
c = []
for i in range(len(b)):
    c.append(b[len(b)-i-1])
for k in range(m):
    for i in range(len(c)):
        if c[i] > 0:
            c[i] = c[i]-1
            print("*", end = "")
        else:
            print(" ", end = "")
    print()