import sys, math, itertools as it, bisect as bi, functools as ft, copy, decimal, heapq as hq
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
S = input().strip()
C_list = list(map(int, input().split()))

tmp_dict = defaultdict(deque)
for i in range(N):
    tmp_dict[int(C_list[i])].append(S[i])

res_dict = defaultdict(deque)
for k, v in tmp_dict.items():
    first_v = v.pop()
    v.appendleft(first_v)
    res_dict[k] = v

res_list = []
for i in range(N):
    res_list.append(res_dict[C_list[i]].popleft())

print("".join(res_list))