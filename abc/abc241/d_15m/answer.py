import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

Q = int(input())

res1_list = SortedList()
res2_list = SortedList()
for j in range(Q):
    input_ = input().split()
    if input_[0] == "1":
        _, x = input_
        x = int(x)
        res1_list.add(-x)
        res2_list.add(x)
    elif input_[0] == "2":
        _, x, k = input_
        x, k = int(x), int(k)
        i = res1_list.bisect_left(-x)
        if i == len(res1_list) or i+k-1 >= len(res1_list):
            print(-1)
        else:
            print(-1*res1_list[i+k-1])
    elif input_[0] == "3":
        _, x, k = input_
        x, k = int(x), int(k)
        i = res2_list.bisect_left(x)
        if i == len(res1_list) or i+k-1 >= len(res2_list):
            print(-1)
        else:
            print(res2_list[i+k-1])