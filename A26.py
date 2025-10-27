from math import sqrt
Q = int(input())
for _ in range(Q):
    X = int(input())
    ex_X = int(sqrt(X))

    for i in range(2, ex_X+1):
        if X % i == 0:
            print('No')
            break
    else:
        print('Yes')
