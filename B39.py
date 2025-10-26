from collections import defaultdict

N, D = map(int, input().split())

XY = defaultdict(list)
for _ in range(N):
    x, y = map(int, input().split())
    
    XY[x].append(y)
print(XY)
ans = 0
for d in range(1, D+1):
    y_mx = max(XY[d])
    XY[d].remove(y_mx)
    print(y_mx)
    ans += y_mx
print(ans)
