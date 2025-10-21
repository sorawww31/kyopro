N, X = map(int, input().split())

# 0 ... N -1
A = list(map(int, input().split()))

l, r = 0, N -1 
while l <= r:
    i = (l + r) // 2
    center = A[i]
    if center > X:
        r = i - 1
    elif center < X:
        l = i + 1
    elif center == X:
        print(i+1)
        break