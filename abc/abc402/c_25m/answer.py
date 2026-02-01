import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2
A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]
B_list = list(map(int, input().split()))

n2i_dict = defaultdict(int)
for i, b in enumerate(B_list, 1):
    n2i_dict[b] = i

res_dict = defaultdict(int)
for A_list in A_lists:
    tmp_res = 1
    for a in A_list[1:]:
        tmp_res = max(n2i_dict[a], tmp_res)

    res_dict[tmp_res] += 1

res = 0
for i in range(1, N+1):
    if i in res_dict:
        res += res_dict[i]
        print(res)
    else:
        print(res)