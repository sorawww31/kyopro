N, A, B = map(int, input().split())

dp = [False for _ in range(100_000 + 1)]

for i in range(min(A, B), N + 1):
    if i >=A and dp[i - A] == False:
        dp[i] = True
    elif i >= B and dp[i-B] == False:
        dp[i] = True

if dp[N]:
    print('First')
else:
    print('Second')