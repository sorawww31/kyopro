# 最大値を求める
class SegTree:
    def __init__(self, n, segfunc, ide_ele):
        self.num = 1 << (n-1).bit_length()
        self.ide_ele = ide_ele # 単位元 MAXを取りたいなら、-無限が単位元
        self.tree = [ide_ele] * self.num * 2 # 
        self.segfunc = segfunc
        # for i in range(n):
        #     self.tree[self.num + i] = init_val[i]
        
        for u in range(self.num -1 , 0, -1):
            self.tree[u] = self.segfunc(self.tree[2*u], self.tree[2*u + 1])
    def update(self, pos, x):
        pos += self.num -1
        
        self.tree[pos] = x

        while pos > 1:
            pos = pos // 2
            self.tree[pos] = self.segfunc(self.tree[2*pos] , self.tree[2*pos + 1])
    
    # l, rは調べたい区間。 a, b はuが持ってる区間
    def query(self, l, r, a, b, u):
        if r <= a or l >= b:
            return self.ide_ele
        elif l <= a and b <= r:
            return self.tree[u]
        else:
            m = (a + b) // 2
            return self.segfunc(self.query(l , r, a, m, 2*u), self.query(l , r, m, b, 2*u+1))

if __name__ == '__main__':
    N, Q = map(int, input().split())
    segtree = SegTree(n=N, segfunc=max, ide_ele=0)
    for _ in range(Q):
        q= list(map(int, input().split()))
        if q[0] == 1:
            segtree.update(q[1], q[2])
        elif q[0] == 2:
            print(segtree.query(q[1], q[2], 1, segtree.num+1, 1))