N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0]*(N)
dp[1] = A[0]
for n in range(2, N):
    dp[n] = min(dp[n-1] + A[n-1], dp[n-2] + B[n-2])
print(dp[N-1])