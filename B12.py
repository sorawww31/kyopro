N = int(input())

def f(x):
    return x**3 + x

# 1 <= N <= 100_000 (int) だから、xは 0 < x < 100 程度(float)

# y軸でNを狭めていく
l, r = 0, 100

while l < r:
    c = (l + r) / 2

    score = f(c)

    if abs(N - score) <= 0.001:
        break
    elif score < N:
        l = c - 0.001
    else:
        r = c + 0.001

print(c)
