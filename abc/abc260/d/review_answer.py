import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, K = map(int, input().split())
P_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = [-1]*N
card_dict = SortedDict()
for t, p in enumerate(P_list, 1):
    i = card_dict.bisect(p)
    if i == len(card_dict):
        card_dict[p] = [p]
    else:
        k, v = card_dict.peekitem(i)
        card_dict[p] = v
        card_dict[p].append(p)
        del card_dict[k]

    if len(card_dict[p]) == K:
        for i in card_dict[p]:
            res_list[i-1] = t
        del card_dict[p]

for res in res_list:
    print(res)