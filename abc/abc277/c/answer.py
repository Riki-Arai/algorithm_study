import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input())

n_set = set()
res_dict = defaultdict(set)
for _ in range(N):
    A, B = map(int, input().split())
    res_dict[A].add(B)
    res_dict[B].add(A)
    n_set.add(A)
    n_set.add(B)

if 1 not in n_set:
    print(1)
    exit()

idx_dict = {x:i for i, x in enumerate(sorted(list(n_set)), 1)}
seen_list = [False]*(len(idx_dict)+1)
res = 0
def dfs(i):
    global res
    idx = idx_dict[i]
    if seen_list[idx]:
        return
    res = max(i, res)
    seen_list[idx] = True
    next_set = res_dict[i]
    for n in next_set:
        dfs(n)

dfs(1)
print(res)