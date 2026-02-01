import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = []
for i in range(N):
    if len(res_list) == 0:
        res = 1
        res_list.append([A_list[i], 1])
        print(res)
        continue

    a = A_list[i]
    pre_a = res_list[-1][0]
    con_n = res_list[-1][1]
    if a == pre_a:
        con_n += 1
        if con_n == a:
            res -= a-1
            res_list.pop()
            print(res)
        else:
            res_list[-1] = [a, con_n]
            res += 1
            print(res)
    else:
        res += 1
        res_list.append([a, 1])
        print(res)