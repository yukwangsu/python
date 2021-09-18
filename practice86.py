T = int(input())
for i in range(T):
    a = input().split(" ")
    d = int(a[1]) - int(a[0])
    stack = 0
    b = 0
    while stack < d:
        b += 1
        stack += b*2
    if d > (stack - b):
        print(b*2)
    else:
        print(b*2-1)