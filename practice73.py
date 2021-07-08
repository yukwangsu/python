N = input()
a = len(N)
N = int(N)
b = []
for j in range(1, N):
    s = j
    J = len(str(j))
    for i in range(J):
        if i == 0:
            s += j % 10
        else: 
            s += (j % 10**(i+1)- j % 10**(i)) // (10**i)
    if s == N:
        b.append(j)
b.append(0)       
print(b[0])