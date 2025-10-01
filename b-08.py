N = int(input())
SIZE = 1501
X_Y = []

for _ in range(N):
    X, Y  = map(int, input().split())
    X_Y.append([X, Y])
max_x = max(point[0] for point in X_Y)
max_y = max(point[1] for point in X_Y)
# min_x = min(point[0] for point in X_Y)
# min_y = min(point[1] for point in X_Y)
K = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
Z = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
# 座標の重複
for X, Y in X_Y:
    K[Y][X] += 1

for x in range(1, max_x+1):
    for y in range(1, max_y+1):
        Z[y][x] = Z[y][x-1] + K[y][x]


for  y in range(1, max_y+1):
    for x in range(1, max_x+1):
        Z[y][x] = Z[y-1][x] + Z[y][x]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(Z[d][c] + Z[b-1][a-1] - Z[d][a-1] - Z[b-1][c])