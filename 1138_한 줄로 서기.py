n = int(input())
re = input().split()
a = [0 for _ in range(n)]
for i in range(n):
    left_b = int(re[i])
    stack = 0
    flag = False
    for k in range(n):
        if stack == left_b:
            for j in range(k, n):
                if a[j] == 0:
                    a[j] = i+1
                    flag = True
                    break
        if a[k] == 0:
            stack += 1
        if flag:
            break
for i in range(n):
    print(a[i], end = ' ')