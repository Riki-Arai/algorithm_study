import math, itertools, bisect, functools
from collections import defaultdict, Counter, deque

N, Q = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(Q)] # 取得例:[[1,2], [3,4]・・[9,10]]

rec_dic = defaultdict(int)
for A_list in A_lists:
    x, y = A_list
    if x == 1:
        rec_dic[y] += 1
    elif x == 2:
        rec_dic[y] += 2
    elif x == 3:
        if rec_dic[y] >= 2:
            print("Yes")
        else:
            print("No")