N, K = map(int, input().split())
A = list(map(int, input().split()))

R = 1

i = 1
j = 0
R = [0 for _ in range(N+1)]
for i in range(N):
    if i == 0:
        R[i] = 1
    else:
        R[i] = R[i-1]

    while R[i] < N and A[R[i] + 1] - A[i] <= K:
        R[i] += 1

print(R)