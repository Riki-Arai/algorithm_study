import sys, math, itertools as it, bisect as bi, functools as ft, copy, decimal, heapq as hq

N, T = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

if len(A_list) == 0:
    print(T)
    exit()

res = 0
w_t = 0
while True:
    b_i = bi.bisect_left(A_list, w_t)
    if b_i >= N:
        break
    res += A_list[b_i]-w_t
    w_t = A_list[b_i] + 100

if len(A_list) and T >= w_t:
    res += T-w_t
    print(res)
else:
    print(res)