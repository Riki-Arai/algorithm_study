import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, L = map(int, input().split()) # 取得例：1 2
D_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

cum_list = [0]
c_dict = defaultdict(set)
c_dict[0].add(1)
for i, d in enumerate(D_list, 2):
    dd = (cum_list[-1] + d)%L
    cum_list.append(dd)
    c_dict[dd].add(i)

p_list = sorted(list(set(cum_list)))
e = L/3
res = 0
for p in p_list:
    p2 = (p+e)
    p3 = (p+2*e)
    p_t = tuple(sorted([p, p2, p3]))
    if p2 in c_dict and p3 in c_dict:
        res += len(c_dict[p])*len(c_dict[p2])*len(c_dict[p3])

print(res)