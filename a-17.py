N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0]*(N)
dp[1] = A[0]
prev = [-1]*(N)
prev[1] = 0
for n in range(2, N):
    if dp[n-1] + A[n-1] < dp[n-2] + B[n-2]:
        dp[n] = dp[n-1] + A[n-1]
        prev[n] = n-1
    else:
        dp[n] = dp[n-2] + B[n-2]
        prev[n] = n-2
output = []
i = N-1
output.append(i)
while i > 0:
    i = prev[i]
    output.append(i)
print(len(output))
print(" ".join([str(r+1) for r in output[::-1]]))