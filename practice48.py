N = int(input())
r = []
for i in range(N):
    t = int(input())
    r.append(t)
for i in range(N):
    changed = False
    for j in range(N-1-i):
        if r[j] > r[j+1]:
            r[j], r[j+1] = r[j+1], r[j]
            changed = True
    if not changed:
        break
    
print(r)
    