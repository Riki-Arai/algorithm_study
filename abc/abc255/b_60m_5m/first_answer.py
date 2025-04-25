N, K = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i in range(N):
    x1, y1 = XY[i]
    lst = []
    for j in range(K):
        x2, y2 = XY[A[j]-1]
        lst.append((x2-x1)**2 + (y2-y1)**2)
    ans = max(ans, min(lst))

print(ans**0.5)


## first
#import math, itertools, bisect, functools, copy
#from collections import defaultdict, Counter, deque
#from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左からROUND_HALF_UPが四捨五入、続いて切り上げ、切り捨て
#
#N, K = map(int, input().split())
#A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#B_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
#
#res = 0
#for i, B_list in enumerate(B_lists, 1):
#    tmp_res = float("INF")
#    x, y = B_list
#    for a in A_list:
#        if i == a:
#            tmp_res = float("INF")
#            break
#        else:
#            xx, yy = B_lists[a-1]
#            tmp_res = min(tmp_res, pow(abs(x-xx), 2) + pow(abs(y-yy), 2))
#
#    if tmp_res != float("INF"):
#        res = max(res, tmp_res)
#
#print(math.sqrt(res))