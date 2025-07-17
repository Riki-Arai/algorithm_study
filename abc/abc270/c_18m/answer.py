import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, X, Y = map(int, input().split())
g_dict = defaultdict(set)
for _ in range(N-1):
    U, V = map(int, input().split())
    g_dict[U].add(V)
    g_dict[V].add(U)


res_list = []
seen_list = [False] * (N+1)
def dfs(i):
    if seen_list[i]:
        return
    seen_list[i] = True
    res_list.append(i)
    for j in g_dict[i]:
        if j == Y:
            res_list.append(j)
            print(*res_list)
            exit()
        dfs(j)
    res_list.pop()

dfs(X)