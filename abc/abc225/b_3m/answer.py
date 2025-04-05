import math, itertools, bisect, functools
from collections import defaultdict, Counter, deque

N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N-1)] # 取得例:[[1,2], [3,4]・・[9,10]]

rec_dic = defaultdict(list)
for A_list in A_lists:
    rec_dic[A_list[0]].append(A_list[1])
    rec_dic[A_list[1]].append(A_list[0])

for v in rec_dic.values():
    if len(v) == N - 1:
        print("Yes")
        exit()
print("No")