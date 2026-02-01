import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split()) # 取得例：1 2

str_dict = defaultdict(list)
res_dict = defaultdict(int)
for i in range(N+1):
    res_dict[i] = i
    str_dict[i] = [""]

for _ in range(Q):
    input_ = input()
    if input_[0] == "1":
        _, p = input_.split()
        p = int(p)
        res_dict[i] = 0
    elif input_[0] == "2":
        _, p, s = input_.split()
        p = int(p)
        str_dict[p].append(s)
    else:
        _, p = input_.split()
        p = int(p)
        str_dict[0] = str_dict[p].copy()

print("".join(str_dict[0]))