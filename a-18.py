N, S = map(int, input().split())
A = list(map(int, input().split()))

#dp = [[False] * (S+1)] * (N+1)
dp = [[False]*(S+1) for _ in range(N+1)]

dp[0][0] = True

A.sort()
for i in range(1, N+1):
    print(f"=================={A[i-1]}==================")
    for s in range(S+1):
        dp[i][s] = dp[i-1][s] or (s >= A[i-1] and dp[i-1][s-A[i-1]])
    for n in range(N+1):
        print(dp[n])
out = "Yes" if dp[N][S] else "No"
print(out)