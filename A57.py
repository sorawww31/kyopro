import math
N, Q = map(int, input().split())
A = list(map(int, input().split()))

#dp[x][i] iの穴から2^x日目にいる位置 0 <= x <= 29, 1<=i<=7 i=0は使わない
dp = [[0 for _ in range(len(A)+1)] for _ in range(30)]

#初期化
for i in range(1, len(A)+1):
    dp[0][i] = A[i-1]

#ダブリング

for x in range(1, 30):
    for i in range(1, len(A)+1):
        dp[x][i] = dp[x-1][dp[x-1][i]]

for _ in range(Q):
    x, y = map(int, input().split())
    pos = x
    for bit in (range(0, int(math.log2(y) +1))):
        if (y >> bit) & 1:
            pos = dp[bit][pos]
    print(pos)