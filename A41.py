N = int(input())
S = input()


for i in range(0, len(S) - 2):
    if S[i] == S[i+1] and S[i] == S[i+2]:
        print('Yes')
        break
else:
    print('No')