N = int(input())
b = []
c = []
for i in range(N):
    a = input().split(" ")
    b.append(int(a[0]))
    c.append(int(a[1]))
z = b[:]
z.sort()
e = list(set(z))
for i in range(len(e)):
    g = []
    for k in range(len(b)):
        if b[k] == e[i]:
            g.append(c[k])
            q = b[k]
    g.sort()
    for l in range(len(g)):
        print(q, g[l])