a = list(input())
score = [0 for _ in range(len(a))]
for i in range(len(a)):
    if a[i] == 'O':
        if a[0] == 'O':
            score[0] = 1
        else:
            score[i] = score[i-1]+1
print(score)
sum = 0
for i in range(len(a)):
    sum += score[i]
print(sum)