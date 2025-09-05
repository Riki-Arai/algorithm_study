import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input()) # 取得例：1
S_list = [input() for _ in range(N)] # 取得例：[A1,A2・・・An]、N行の入力用

c = Counter(S_list)
max_v = c.most_common()[0][1]
res_list = []
for k, v in c.items():
    if v == max_v:
        res_list.append(k)

res_list.sort()
for res in res_list:
    print(res)