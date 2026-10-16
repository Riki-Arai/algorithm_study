'''
(1) グラフで削除の操作は難しいことが多いと思われるので追加をする方向で解くことを考える（この考え方は使えることが多い）
(2) また1~kまでを行き来することができるということは、それらは1つの部分グラフとして連結していることと同値
(3) そして図で書いて考察をしていくうちに、kごとに確認をしていきkより大きいものを削除し、k以下のものはDSUに追加すればいいことに気づく
(4) 削除の問題→追加で考える、お互いに行き来できる→連結という変換をする視点を持ってみることが大事
'''
from atcoder.dsu import DSU

N, M = map(int, input().split()) # 取得例：1 2

n2ns_lists = [set() for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split()) # 取得例：1 2
    n2ns_lists[u].add(v)
    n2ns_lists[v].add(u)

dsu = DSU(N+1)
del_set = set()
for k in range(1, N+1):
    if k in del_set:
        del_set.discard(k)

    if k == 1:
        for u in n2ns_lists[k]:
            del_set.add(u)
    else:
        for u in n2ns_lists[k]:
            if u > k:
                del_set.add(u)
            else:
                dsu.merge(u, k)

    if dsu.size(k) == k:
        print(len(del_set))
    else:
        print(-1)