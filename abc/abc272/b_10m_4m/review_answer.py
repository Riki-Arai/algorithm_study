import math, itertools, bisect, functools
from collections import defaultdict, Counter, deque

N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

all_c_set = set(itertools.combinations([i for i in range(1, N)], 2))
for A_list in A_lists:
    all_c_set.difference_update(set(itertools.combinations(A_list[1:], 2)))

if len(all_c_set) == 0:
    print("Yes")
else:
    print("No")


### first
#import math, itertools, bisect, functools
#from collections import defaultdict, Counter, deque
#
#N, M = map(int, input().split())
#A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]
#
#all_c_list = list(itertools.combinations([i for i in range(1, N)], 2))
#for A_list in A_lists:
#    for x in itertools.combinations(A_list[1:], 2):
#        if x in all_c_list:
#            all_c_list.remove(x)
#
#if len(all_c_list) == 0:
#    print("Yes")
#else:
#    print("No")
#