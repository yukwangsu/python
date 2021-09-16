from collections import deque
import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    x = deque(sys.stdin.readline().rstrip())
    array = deque()
    num = []
    sum = 0
    x.popleft()
    for j in range(len(x)):
        if x[0] == ",":
            for k in range(len(num)):
                sum += num[k]*10**(len(num)-k-1)
            array.append(int(sum))
            x.popleft()
            num = []
            sum = 0
        elif x[0] == "]":
            for k in range(len(num)):
                sum += num[k]*10**(len(num)-k-1)
            array.append(int(sum))
            x.popleft()
            num = []
            sum = 0
        else:
            num.append(int(x[0]))
            x.popleft()
    d = 0
    for j in range(len(p)):
        if p[j] == "D":
            d += 1
    if d > n:
        print("error")
    elif d == n:
        print("[]")
    else:
        r = 0
        for j in range(len(p)):
            if p[j] == "D":
                if r % 2 == 0:
                    array.popleft()
                else:
                    array.pop()
            else: 
                r += 1
        if r % 2 == 0:
            print("[", end = "")
            for j in range(len(array)-1):
                print(array[j], end = ",")
            print(array[-1], end = "]\n")
        else:
            print("[", end = "")
            for j in range(len(array)-1):
                print(array[len(array)-j-1], end = ",")
            print(array[0], end = "]\n")