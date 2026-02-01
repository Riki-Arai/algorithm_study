from sortedcontainers import SortedSet

Q = int(input())

N = 2 ** 20
A = [-1] * N
ss = SortedSet(range(N)) # Aの要素が-1であるもののインデックスの集合
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        # Aの第x項以降にある最初の-1を、x書き換える
        idx = ss.bisect_left(x % N) # x>=N の可能性があるので x%N にする
        if idx == len(ss):
            idx = 0
        A[ss[idx]] = x
        ss.discard(ss[idx])
    elif t == 2:
        print(A[x % N])

#from collections import defaultdict
#
#Q = int(input())
#N = 2**20
#
#res_dict = defaultdict(int)
#res_list = [-1]*N
#for _ in range(Q):
#    t, x = map(int, input().split())
#    r = x%N
#    if t == 1:
#        if res_list[r] != -1:
#            while res_list[r] != -1:
#                res_dict[r] += 1
#                r = (r+res_dict[r]-1)%N
#            res_list[r] = x
#            res_dict[r] += 1
#        else:
#            res_list[r] = x
#            res_dict[r] += 1
#    else:
#        print(res_list[r])