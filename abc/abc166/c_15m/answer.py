import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2
H_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

res_list = [True] * (N+1)
h_dict = defaultdict(int)
for i, h in enumerate(H_list, 1):
    h_dict[i] = h

for a, b in A_lists:
    if h_dict[a] == h_dict[b]:
        res_list[a] = False
        res_list[b] = False
    elif h_dict[a] > h_dict[b]:
        res_list[b] = False
    elif h_dict[a] < h_dict[b]:
        res_list[a] = False

print(res_list[1:].count(True))