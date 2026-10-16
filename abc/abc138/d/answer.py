'''
(1) 1を根にした木なので、回路を持たずに上から下に降るイメージ
(2) Q回ごとに木を探索するとTLEとなるので、先にQ回分の操作で点に重みを付与してからスコアを伝搬すると良さそう
(3) 最初はBFSをやっていたが、バックトラックによる累積和の調整が便利な点を踏まえてDFSに切り替えて解いた
'''
import sys
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split()) # 取得例：1 2

g_lists = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split()) # 取得例：1 2
    g_lists[a].append(b)
    g_lists[b].append(a)

w_list = [0]*(N+1)
for _ in range(Q):
    p, x = map(int, input().split()) # 取得例：1 2
    w_list[p] += x

res_list = [0]*(N+1)
seen_set = set([1])
def dfs(a, cum):
    res_list[a] = cum
    for b in g_lists[a]:
        if b not in seen_set:
            seen_set.add(b)
            dfs(b, cum+w_list[b])

dfs(1, w_list[1])
print(*res_list[1:])