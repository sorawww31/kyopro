N, M = map(int, input().split())

#隣接リスト
G = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)
C = [False]*(N+1)

def dfs(pos):
    C[pos] = True
    for nex in G[pos]:
        if C[nex] == False:
            dfs(nex)
    return
dfs(1)
for i in range(1, N+1):
    if C[i] == False:
        print("The graph is not connected.")
        break
else:
    print("The graph is connected.")