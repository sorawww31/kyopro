N = int(input())
A = list(map(int, input().split()))
D = int(input())
L_MAX = A.copy()
R_MAX = A.copy()

for i in range(1, N):
    j = N - i - 1
    L_MAX[i] = max(L_MAX[i], L_MAX[i-1])
    R_MAX[j] = max(R_MAX[j], R_MAX[j+1])

for _ in range(D):
    L, R = map(int, input().split())
    L-=1
    R-=1
    print(max(L_MAX[L-1], R_MAX[R+1]))