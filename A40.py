from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

S = defaultdict(lambda: 0)
# aCbの計算 
def cmb(a:int, b:int):
    ue = 1
    shita = 1
    b = b if a // 2 > b else a - b
    for i in range(0, b): 
        ue *= a - i
        shita *= i+1
    return int(ue / shita)

for a in A:
    S[a] += 1

ans = 0
for v in S.values():
    if v >= 3:
        ans += cmb(v, 3)
print(ans)