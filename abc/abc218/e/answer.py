'''
(1) 連結成分に関する問題なのでDSUを使うことを念頭に置く
(2) DSUは追加しかできないので逆の手順で解くことを検討
(3) 最初に全て削除し、連連ではない頂点同士で値が少ないものから追加する
    →ただし連結済みでも負のものは強制的に追加
(4) 全ての点が一つに連結できたかどうかの判定方法があまり理解できていなかったのでそちらを学べた
'''
import heapq as hq
from atcoder.dsu import DSU

N, M = map(int, input().split()) # 取得例：1 2

hq_lists = []
hq.heapify(hq_lists)
sum_ = 0
for _ in range(M):
    A, B, C = map(int, input().split()) # 取得例：1 2
    sum_ += C
    hq.heappush(hq_lists, (C, A, B))

res = 0
dsu = DSU(N+1)
while len(hq_lists):
    c, a, b = hq.heappop(hq_lists)
    if not dsu.same(a, b):
        dsu.merge(a, b)
        sum_ -= c
        if dsu.size(a) == N:
            res = max(sum_, res)
    elif dsu.same(a, b) and c < 0:
        sum_ -= c
        if dsu.size(a) == N:
            res = max(sum_, res)

print(res)