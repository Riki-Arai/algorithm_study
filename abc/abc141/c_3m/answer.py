import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, K, Q = map(int, input().split()) # 取得例：1 2
A_list = [int(input()) for _ in range(Q)] # 取得例：[A1,A2・・・An]、N行の入力用(int型に変換)

res_dict = defaultdict(int)
for a in A_list:
    res_dict[a] += 1

for i in range(1, N+1):
    if K - (Q-res_dict[i]) > 0:
        print("Yes")
    else:
        print("No")