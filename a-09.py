H, W, N = map(int, input().split())

K = [[0 for _ in range(W+2)] for _ in range(H+2)]

for _ in range(N):
    A, B, C, D = map(int, input().split())
    K[A][B] += 1
    K[C+1][D+1] += 1
    K[C+1][B] -= 1
    K[A][D+1] -= 1

Z = [[0 for _ in range(W+2)] for _ in range(H+2)]

for x in range(1, W + 1):
    for y in range(1, H+1):
        Z[y][x] = Z[y-1][x] + K[y][x]

for y in range(1, H+1):
    for x in range(1, W+1):
        Z[y][x] = Z[y][x-1] + Z[y][x]

for z in Z[1: H+1]:
    l = [str(n) for n in z[1:W+1]]
    print(" ".join(l))