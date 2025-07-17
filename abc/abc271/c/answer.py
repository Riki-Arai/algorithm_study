import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, X, Y = map(int, input().split())
e_dict = defaultdict(set)
for _ in range(N):
    U, V = map(int, input().split())
    e_dict[U].add(V)
    e_dict[V].add(U)

res_list = []
n_list = [False] * (N+1)
def dfs(i):
    if n_list[i]:
        return
    n_list[i] = True
    res_list.append(i)
    for e in e_dict[i]:
        if e == Y:
            break
        dfs(e)

dfs(X)
print(*res_list)