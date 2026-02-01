### 自分の解答
N, M = map(int, input().split())
A_list = sorted(map(int, input().split()))

sum_ = sum(A_list)
res = sum_
A_list = A_list*2
cum_ = 0
count = 0
for i in range(2*N-1):
    n = A_list[i]
    nn = A_list[i+1]
    count += 1
    cum_ += n
    if not(n == nn or (n+1)%M == nn) or count == N:
        res = min(sum_-cum_, res)
        count = 0
        cum_ = 0

print(res)


### 参考になった解答
n, m = map(int, input().split())
A = sorted(map(int, input().split()))
A *= 2

total = sum(A[:n])
cum = 0
cnt = 0
ans = total
for i in range(2 * n):
    # A_list[-1]からスタートしたことになっても問題ない
    if A[i] == A[i - 1] or A[i] == (A[i - 1] + 1) % m:
        cum += A[i]
        cnt += 1
    else:
        cum = A[i]
        cnt = 1
    if cnt <= n:
        ans = min(ans, total - cum)

print(ans)

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
#N, M = map(int, input().split())
#A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#sum_ = 0
#A_list.sort()
#dq = deque()
#for l in range(N):
#    tmp_sum = 0
#    dq.append(A_list[l])
#    while len(dq) >= 2 and not (dq[-2] == dq[-1] or (dq[-2]+1)%M == dq[-1]):
#        tmp_sum += dq.popleft()
#    sum_ = max(tmp_sum, sum_)
#
#res_list = []
#while len(dq):
#    pop_n = dq.popleft()
#    if len(res_list) and (res_list[-1] == pop_n or (res_list[-1]+1)%M == pop_n):
#        res_list.append(pop_n)
#    else:
#        res_list.append(pop_n)
#sum_ = max(sum(res_list), sum_)
#f_res = sum(A_list)-sum_
#
#tar_i = None
#for i in range(N-1, -1, -1):
#    if not(A_list[i-1] == A_list[i] or A_list[i-1]+1 == A_list[i]):
#        tar_i = i
#        break
#
#if tar_i != None:
#    sum_ = 0
#    B_list = A_list[tar_i:] + A_list[:tar_i]
#    #dq = deque()
#    for l in range(len(B_list)):
#        tmp_sum = 0
#        dq.append(B_list[l])
#        while len(dq) >= 2 and not (dq[-2] == dq[-1] or (dq[-2]+1)%M == dq[-1]):
#            tmp_sum += dq.popleft()
#
#        sum_ = max(tmp_sum, sum_)
#
#    res_list = []
#    while len(dq):
#        pop_n = dq.popleft()
#        if len(res_list) and (res_list[-1] == pop_n or (res_list[-1]+1)%M == pop_n):
#            res_list.append(pop_n)
#        else:
#            res_list.append(pop_n)
#    sum_ = max(sum(res_list), sum_)
#
#    print(min(sum(A_list)-sum_, f_res))
#
#else:
#    print(f_res)