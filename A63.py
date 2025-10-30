N, M = map(int, input().split())

#隣接リスト
G = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

