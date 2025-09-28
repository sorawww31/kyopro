S = input()
T = input()

dp = [[0]*(len(T)+1) for _ in range(len(S)+1) ]

for s in range(len(S)):
    for t in range(len(T)):
        if S[s] == T[t]:
            dp[s+1][t+1] = dp[s][t] + 1
        else:
            dp[s+1][t+1] = max(dp[s][t+1], dp[s+1][t])
        print(dp)
print(dp[len(S)][len(T)])    