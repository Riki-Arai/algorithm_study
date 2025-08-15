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
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
C_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_dict = defaultdict(int)
res_set = set()
for i in range(N):
    res_set.add(B_list[C_list[i]-1])
    res_dict[B_list[C_list[i]-1]] += 1

res = 0
for a in A_list:
    if a in res_set:
        res += res_dict[a]

print(res)