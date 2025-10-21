N = int(input())
SIZE = 5
K = [[0 for _ in range(SIZE+1)] for _ in range(SIZE + 1)]
Z = [[0 for _ in range(SIZE+1)] for _ in range(SIZE + 1)]

for _ in range(N):
    A, B, C, D = map(int, input().split())
    K[A][B] += 1
    K[C][D] += 1
    K[A][D] -= 1
    K[C][B] -= 1


for x in range(0, SIZE+1):
    for y in range(0, SIZE):
        Z[x][y+1] = Z[x][y] + K[x][y]

for y in range(0, SIZE+1):
    for x in range(0, SIZE):
        Z[x+1][y] = Z[x+1][y] + Z[x][y]

score = 0
for x in range(SIZE+1):
    for y in range(SIZE+1):
        score += 1 if Z[x][y] > 0 else 0
print(score)