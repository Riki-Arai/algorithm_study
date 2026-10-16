'''
※GPTに修正をしてもらってAC
(1) 余ったものを別の連結成分に繋げる考察は比較的すぐにできた
(2) 下のコードのwhile以降の実装がうまくできず
(3) 「if not dsu.same(a, x):」をせずに複雑に管理をしていたので、それが一つの原因ではある
(4) g_setの使い方についても、現在残っているグループの集合として扱っていくべきだった
(5) 総じて体系的に処理を落とし込めずにいきあたりばったりなままに実装をしてしまったことが敗因
'''
import heapq as hq
from atcoder.dsu import DSU

N, M = map(int, input().split())

dsu = DSU(N + 1)
hq_lists = []
g_set = set()
for i in range(1, M + 1):
    A, B = map(int, input().split())

    if dsu.same(A, B):
        hq.heappush(hq_lists, (dsu.leader(A), i, A, B))
    else:
        dsu.merge(A, B)

for n in range(1, N + 1):
    g_set.add(dsu.leader(n))

res_lists = []
while len(g_set) > 1:
    g, i, a, b = hq.heappop(hq_lists)

    gg = -1
    # a が属する連結成分とは異なる連結成分を探す
    for x in g_set:
        if not dsu.same(a, x):
            gg = x
            break

    # 必ず見つかる
    res_lists.append((i, a, gg))

    # merge 前の leader を保存
    g = dsu.leader(a)
    gg = dsu.leader(gg)

    dsu.merge(a, gg)

    # merge 後の leader に合わせて g_set を更新
    g_set.discard(g)
    g_set.discard(gg)
    g_set.add(dsu.leader(a))

print(len(res_lists))
for res_list in res_lists:
    print(*res_list)