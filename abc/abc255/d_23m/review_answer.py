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
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

A_list.sort()
sum_ = sum(A_list)
cum_list = [0]
for a in A_list:
    cum_list.append(cum_list[-1]+a)

for _ in range(Q):
    X = int(input())
    l_i = bisect.bisect_left(A_list, X)
    r_i = bisect.bisect_right(A_list, X)
    print((l_i*X-cum_list[l_i]) + ((cum_list[N]-cum_list[r_i])-(N-r_i)*X))