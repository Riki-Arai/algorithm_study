import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左からROUND_HALF_UPが四捨五入、続いて切り上げ、切り捨て

N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

l_lists = []
for a in A_list:
    l_lists.append(B_lists[a-1])

res_list = []
for B_list in B_lists:
    tmp_list = []
    x, y = B_list
    for l_list in l_lists:
        xx, yy = l_list
        if (xx != x and yy != y) and B_list not in l_lists:
            tmp_list.append(pow(abs(x-xx), 2) + pow(abs(y-yy), 2))

    if len(tmp_list) > 0:
        res_list.append(min(tmp_list))

print(math.sqrt(max(res_list)))