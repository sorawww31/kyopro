from collections import deque
Q = int(input())
S = deque()
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        S.append(q[1])
    elif q[0] == '2':
        print(S[-1])
    elif q[0] == '3':
        S.pop()