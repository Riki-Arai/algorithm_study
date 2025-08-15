import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

i2n_dict = defaultdict(int)
n2i_dict = defaultdict(int)
for i, a in enumerate(A_list):
    i2n_dict[i] = a
    n2i_dict[a] = i

res_sets = set()
for j in range(1, N+1):
    i = n2i_dict[j]
    n = i2n_dict[j-1]
    ni = n2i_dict[n]
    n2i_dict[j], i2n_dict[ni] = ni, j
    n2i_dict[n], i2n_dict[i] = i, n
    if i+1 != ni+1:
        res_sets.add((ni+1, i+1))

res_lists = sorted(list(res_sets), key=lambda x: x[0])
print(len(res_lists))
for res_list in res_lists:
    print(*res_list)