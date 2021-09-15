answer = 0
M = int(input())
for i in range(M):
    N = str(M)
    N.split(" ")
    array = []
    s = 0
    for j in range(len(N)):
        array.append(int(N[j]))
    if len(array) <= 2:
        s = 1
    else:
        d = array[0] - array[1]
        for k in range(len(array)-1):
            if d == array[k] - array[k+1]: 
                s = 1
            else:
                s = 0
                break
    if s == 1:
        answer += 1
        M -= 1
    else:
        M -= 1
print(answer)