num = 0
while True:
    num += 1
    a = input().split()
    L, P, V = int(a[0]), int(a[1]), int(a[2])
    if L == 0 and P == 0 and V == 0:
        break
    else:
        if V % P < L:
            m = V//P*L + V%P 
        else:
            m = V//P*L + L
    print(f'Case {num}: {m}')