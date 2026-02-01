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
X_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res_list = []
box_list = [0] * N
min_v = float("INF")
for x in X_list:
    if x == 0:
        for i, x in enumerate(box_list, 1):
            if x <= min_v:
                res_list.append(i)
                box_list[i-1] += 1
                break
        else:
            res_list.append(1)
            box_list[0] += 1
        min_v = min(box_list)
    else:
        res_list.append(x)
        box_list[x-1] += 1
        min_v = min(box_list)

print(*res_list)