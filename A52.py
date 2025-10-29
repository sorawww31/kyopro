from collections import deque

N = int(input())
S = deque()

for _ in range(N):
    q = input().split()
    if q[0] == '1':
        S.append(q[1])
    elif q[0] == '2':
        print(S[0])
    elif q[0] == '3':
        S.popleft()