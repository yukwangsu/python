

a = input().split(" ")
N = int(a[0])
X = int(a[1])

P = input().split(" ")

for p in P:   
    if int(p) < X:
        print(p, end = " ")
