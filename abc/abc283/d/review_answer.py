import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

S = input().strip()

res_list = [""]
res_set = set()
for s in S:
    if s == ")":
        pop_res = res_list.pop()
        for x in pop_res:
            res_set.discard(x)
    elif s == "(":
        res_list.append("")
    else:
        res_list[-1] += s
        if s in res_set:
            print("No")
            exit()
        else:
            res_set.add(s)

print("Yes")