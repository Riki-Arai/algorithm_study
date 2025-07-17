N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

p_lists = [[False]*N for _ in range(N)]
for A_list in A_lists:
    c_a_list = A_list[1:].copy()
    for i in range(len(c_a_list)):
        a = c_a_list[i]
        for j in range(len(c_a_list)):
            b = c_a_list[j]
            p_lists[a-1][b-1] = True
            p_lists[b-1][a-1] = True

for p_list in p_lists:
    if not all(p_list):
        print("No")
        exit()

print("Yes")


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