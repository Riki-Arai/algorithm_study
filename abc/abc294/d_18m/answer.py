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

n = 1
res_list = []
call_set = SortedSet()
for _ in range(Q):
    input_ = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
    if input_[0] == 1:
        call_set.add(n)
        n += 1
    elif input_[0] == 2:
        _, x = input_
        call_set.discard(x)
    else:
        res_list.append(call_set[0])

for res in res_list:
    print(res)