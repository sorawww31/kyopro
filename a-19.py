N, W = map(int, input().split())

weights, values = [], []

dp = [[0] * (W+1) for _ in range(N+1)]

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)
for i in range(1, N+1):
    for w in range(W+1):
    
        if w - weights[i-1] < 0:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w-weights[i-1]] + values[i-1], dp[i-1][w])

print(dp[N][W])
