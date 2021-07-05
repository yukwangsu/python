def sorting(a):
    b = [a[i] for i in range(len(a))]
    b.sort()
    return b
import sys
a = list(map(int, sys.stdin.readline().split()))
print(sorting(a))
print(a)