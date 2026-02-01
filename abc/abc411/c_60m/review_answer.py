# 白→黒の境目の数を保存して答えていくことがポイント
N, Q = map(int, input().split())
A_list = list(map(int, input().split()))

c = [0] * (N + 2)
ans = 0
def add(i: int, x: int):
    global ans
    if 0 <= i < N + 1:
        if c[i] == 0 and c[i+1] == 1:
            ans += x

for a in A_list:
    ### 現時点で白→黒の並びに該当する場合は-1をしていく
    # 白(左側)→黒(反反対象)であれば白に反転することで境目が消えるので-1
    add(a-1, -1)
    # 白(反転対象)→黒(右側)であれば黒に反転することで境目が消えるので-1
    add(a, -1)

    c[a] = 1 - c[a]

    add(a-1, 1)
    add(a, 1)

    print(ans)

# first
#import sys, math, itertools, bisect, functools, copy, decimal
#from more_itertools import distinct_permutations
#from functools import cmp_to_key
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from sortedcontainers import SortedSet, SortedList, SortedDict
#from collections import defaultdict, Counter, deque
#from atcoder.dsu import DSU
#sys.setrecursionlimit(10**7)
#
#N, Q = map(int, input().split()) # 取得例：1 2
#A_list = list(map(int, input().split()))
#
#res = 0
#if N == 1:
#    for i in range(Q):
#        if i%2 == 1:
#            print(0)
#        else:
#            print(1)
#    exit()
#
#res_list = [False] * N
#for a in A_list:
#    i = a-1
#    if i == 0:
#        if not res_list[i]:
#            if res_list[i+1]:
#                res_list[i] = True
#            elif not res_list[i+1]:
#                res_list[i] = True
#                res += 1
#            print(res)
#        else:
#            if res_list[i+1]:
#                res_list[i] = False
#            elif not res_list[i+1]:
#                res_list[i] = False
#                res -= 1
#            print(res)
#    elif i == N-1:
#        if not res_list[i]:
#            if res_list[i-1]:
#                res_list[i] = True
#            elif not res_list[i-1]:
#                res_list[i] = True
#                res += 1
#            print(res)
#        else:
#            if res_list[i-1]:
#                res_list[i] = False
#            elif not res_list[i-1]:
#                res_list[i] = False
#                res -= 1
#            print(res)
#    else:
#        if not res_list[i]:
#            if i-1 >= 0 and i+1 < N and res_list[i-1] and res_list[i+1]:
#                res_list[i] = True
#                res = max(res-1, 0)
#            elif i-1 >= 0 and i+1 < N and not res_list[i-1] and not res_list[i+1]:
#                res_list[i] = True
#                res += 1
#            else:
#                res_list[i] = True
#            print(res)
#        else:
#            if i-1 >= 0 and i+1 < N and res_list[i-1] and res_list[i+1]:
#                res_list[i] = False
#                res += 1
#            elif i-1 >= 0 and i+1 < N and not res_list[i-1] and not res_list[i+1]:
#                res_list[i] = False
#                res -= 1
#            else:
#                res_list[i] = False
#            print(res)