import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())

b_dict = defaultdict(int)
n_dict = defaultdict(set)
for i in range(1, N+1):
    b_dict[i].add(i)
    n_dict[i] = i

for _ in range(Q):
    X_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
    if X_list[0] == 1:
        _, a, b = X_list
        b_dict[a] = b
        n_dict[b].add(a)
        n_dict[a].discard(a)
    elif X_list[0] == 2:
        _, a, b = X_list
    else:
        _, a = X_list
        print(b_dict[a])