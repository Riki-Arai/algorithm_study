import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左からROUND_HALF_UPが四捨五入、続いて切り上げ、切り捨て

N = int(input())

A_lists = []
for _ in range(N):
    input()
    A_lists.append(list(map(int, input().split())))

X = int(input())
min_v = float("INF")
res_dic = defaultdict(list)
for i, A_list in enumerate(A_lists, 1):
    if X in A_list:
        res_dic[len(A_list)].append(i)
        min_v = min(min_v, len(A_list))

print(len(res_dic[min_v]))
print(*res_dic[min_v])

#N = int(input())
#
#A_lists = []
#for _ in range(N):
#    C = int(input())
#    A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#    A_lists.append(A_list)
#
#X = int(input())
#res_dic = {}
#min_v = 100
#for i, A_list in enumerate(A_lists, 1):
#    if X in A_list:
#        if len(A_list) not in res_dic:
#            res_dic[len(A_list)] = [i]
#        else:
#            tmp_list = res_dic[len(A_list)]
#            tmp_list.append(i)
#            res_dic[len(A_list)] = tmp_list
#        min_v = min(min_v, len(A_list))
#
#if min_v not in res_dic:
#    print(0)
#    print()
#else:
#    res_list = res_dic[min_v]
#    res_list.sort()
#    print(len(res_list))
#    print(*res_list)