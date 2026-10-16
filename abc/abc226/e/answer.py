'''
(1) グラフを描いて考察をしている中で閉路が1つのケースの時に条件を満たせることがまずわかった
(2) さらに続けて(1)のケースの場合は2個なので、連結成分ごとに2倍ずつすればいい
(3) しかし下の回答は少々不十分で枝の数=頂点の数（閉路が1つの場合）で解いた方がより筋が良かった
(4) 図を描くだけではなく枝や頂点の数に着目する、閉路の数に着目する手順が大事だと学んだ
'''
from atcoder.dsu import DSU

N, M = map(int, input().split()) # 取得例：1 2

MOD = 998244353
dsu = DSU(N+1)
g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    U, V = map(int, input().split()) # 取得例：1 2
    uv_list = sorted([U, V])
    g_lists[uv_list[0]].append(uv_list[1])
    dsu.merge(U, V)

res = 1
dsu_2 = DSU(N+1)
seen_set = set() # 頂点の一部がどれとも連結していないケースで必要
for g in list(dsu.groups()):
    if len(g) >= 2:
        count = 0
        for u in g:
            seen_set.add(u)
            for v in g_lists[u]:
                seen_set.add(v)
                if dsu_2.same(u, v):
                    count += 1
                else:
                    dsu_2.merge(u, v)
        if count == 1:
            res = (res*2)%MOD
        else:
            print(0)
            exit()

if len(seen_set) == N:
    print(res%MOD)
else:
    print(0)