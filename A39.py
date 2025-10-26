N = int(input())

L_R = []
for _ in range(N):
    l, r = map(int, input().split())
    L_R.append((l, r))

# Rでソート
L_R.sort(key=lambda x: x[1])

current_time = 0
Ans = []
for l, r in L_R:
    # 選べる
    if current_time <= l:
        current_time = r
        Ans.append((l, r))

print(len(Ans))


