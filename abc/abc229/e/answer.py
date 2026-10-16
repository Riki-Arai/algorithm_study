'''
※解説AC
(1) 逆から処理をしてDSUを使うこと自体はすぐに思いついてはいた
(2) GPTに聞いてわかったが、A<Bの関係になっていることが地味に重要だった
(3) 無向グラフだからといって双方からアクセスできるようにする必要はないことが学べた
(4) またDSU+削除のような問題は逆から攻めることを意識するべき
'''
from atcoder.dsu import DSU

N, M = map(int, input().split()) # 取得例：1 2

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split()) # 取得例：1 2
    g_lists[A].append(B)

res_list = []
res = 0
dsu = DSU(N+1)
for a in range(N, 0, -1):
    res_list.append(res)
    res += 1
    for b in g_lists[a]:
        if not dsu.same(a, b):
            dsu.merge(a, b)
            res -= 1

for res in reversed(res_list):
    print(res)