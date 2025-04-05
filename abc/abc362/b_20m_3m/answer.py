import math, itertools, bisect, functools
from collections import defaultdict, Counter, deque

A_lists = [list(map(int, input().split())) for _ in range(3)] # 取得例:[[1,2], [3,4]・・[9,10]]

res_list = []
for c in itertools.combinations(A_lists, 2):
    x1, y1 = c[0][0], c[0][1]
    x2, y2 = c[1][0], c[1][1]
    res_list.append(pow(abs(x1-x2), 2)+pow(abs(y1-y2), 2))

max_v = max(res_list)
res_list.remove(max_v)
if max_v == sum(res_list):
    print("Yes")
else:
    print("No")