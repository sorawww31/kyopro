N , K = map(int, input().split())
A = list(map(int, input().split()))

def check(x: int): # 答えがx以下か判定する
    cnt = 0
    for a in A:
        cnt += x // a
    
    if cnt >= K:
        return True
    else:
        return False
    
def main():
    l, r = 0, 1000_000_000
    while l < r:
        x = (l+r) // 2
        boolian = check(x)
        
        if boolian:
            r = x
        else:
            l = x + 1
    print(l)

if __name__ == "__main__":
    main()