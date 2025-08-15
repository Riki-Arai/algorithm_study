# 一度利用したインデックスは-1してあげる
import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

S = input().strip()

alp_dict = defaultdict(int)
for i, s in enumerate(S):
    alp_dict[s] += 1

res = 0
if max(alp_dict.values()) >= 2:
    res += 1

for i, s in enumerate(S):
    for k, v in alp_dict.items():
        if k != s:
            res += v
    if alp_dict[s] - 1 >= 0:
        alp_dict[s] -= 1

print(res)


## 以下は自分の回答
#S = input().strip()
#alp_dict = {chr(i):0 for i in range(ord('a'), ord('z') + 1)}
#for s in S:
#    alp_dict[s] += 1
#
#res = 0
#sum_ = len(S)
#if max(list(alp_dict.values())) > 1:
#    res += 1
#
#for i, s in enumerate(list(S), 1):
#    n = alp_dict[s] - 1
#    res += sum_ - n - i
#    alp_dict[s] = n
#
#print(res)