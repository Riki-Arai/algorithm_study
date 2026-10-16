'''
※C++でAC
(1) グラフで連結に関する問題はDSUとグループIDを使用し、さらに大きさが絡むのでソートはほぼ必要になることを念頭に置く
(2) kは10番以下までしか指定しないので10番目までを常に持っておけばいい
(3) なのでQ回の処理が大きくても、クエリ1の処理でごちゃごちゃとやってもせいぜい計算量は10程度で済む
(4) pythonだとTLEになってしまったのでC++でACした
(5) 連結が絡むときはDSUとグループIDを用いること、k番目が小さいことがたまにあるのでそこに注意することを学ぶ
'''
#  SortedListは「key=lambda x: -x」で降順にできる。SortedDictはlistやsetの値を持てる、peekitem(bisect_left(1))のイメージで1に近いキーの値を取得可能
from sortedcontainers import SortedSet
from collections import defaultdict
from atcoder.dsu import DSU

N, Q = map(int, input().split()) # 取得例：1 2

dsu = DSU(N+1)
g2ns_dict = defaultdict(SortedSet)
for n in range(1, N+1):
    g2ns_dict[dsu.leader(n)] = SortedSet([-n])

for _ in range(Q):
    input_ = input()
    if input_[0] == "1":
        _, u, v = map(int, input_.split())
        if dsu.same(u, v):
            continue

        u_set = g2ns_dict[dsu.leader(u)]
        u_set.add(-u)
        v_set = g2ns_dict[dsu.leader(v)]
        v_set.add(-v)

        u_gid = dsu.leader(u)
        v_gid = dsu.leader(v)
        dsu.merge(u, v)
        u_set.update(v_set)
        while len(u_set) > 10:
            u_set.pop()

        new_gid = dsu.leader(u)
        g2ns_dict[new_gid] = u_set.copy()
        if u_gid == new_gid:
            g2ns_dict[v_gid] = SortedSet()
        else:
            g2ns_dict[u_gid] = SortedSet()
    else:
        _, v, k = map(int, input_.split())
        gid = dsu.leader(v)
        if k <= len(g2ns_dict[gid]):
            print(-1*g2ns_dict[gid][k-1])
        else:
            print(-1)