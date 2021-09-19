N = int(input())
a = input().split(' ')
max = int(a[0])
answer = 0
b = 0
for i in range(N):
    if int(a[i]) >= max:
        max = int(a[i])
        if b > answer:
            answer = b
            b = 0
        else:
            b = 0
    else:
        if i == (N-1):
            b += 1
            if b > answer:
                answer = b
        else:    
            b += 1
print(answer)