A = int(input())
B = int(input())
C = int(input())
a = str(A*B*C)
a = list(a)
for i in range(10):
    b = 0
    for j in range(len(a)):
        if i == int(a[j]):
            b += 1
    print(b)