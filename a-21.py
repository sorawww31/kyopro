N = int(input())
P, A = [0], [0]

for _ in range(N):
    p, a = map(int, input().split())
    P.append(p)
    A.append(a)

dp = [ [0 for _ in range(N+1)] for _ in range(N+1)]

for length in range(2, N+1):
    for l in range(1, N - length + 2):   # ← l は 1 始まり
        r = l + length - 1               # ← r も 1..N
        left_point  = A[l] if l < P[l] <= r else 0
        right_point = A[r] if l <= P[r] <  r else 0
        dp[l][r] = max(dp[l+1][r] + left_point, dp[l][r-1] + right_point)

print(dp[1][N])