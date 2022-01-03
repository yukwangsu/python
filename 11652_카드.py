import sys 
n = int(sys.stdin.readline().rstrip())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline().rstrip()))
a.sort()
max_stack = 0
stack = 1
pre = a[0]
m_card = a[0]
for i in range(1, n):
    if a[i] == pre:
        stack += 1
        if stack > max_stack:
            max_stack = stack
            m_card = a[i]
    else:
        stack = 1
        pre = a[i]
print(m_card)