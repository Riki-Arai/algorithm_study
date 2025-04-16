import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左からROUND_HALF_UPが四捨五入、続いて切り上げ、切り捨て

N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
for i in range(N):
    a = A_list[i]
    bi_idx = 0
    while True:
        bi_idx = bisect.bisect_right(A_list[bi_idx:], a//2)
        if a >= 2 * A_list[bi_idx]:
            if bi_idx+1 < N and a >= 2 * A_list[bi_idx+1]:
                continue
            else:
                break
        elif a < 2 * A_list[bi_idx]:
            #r_idx -= 1
            break

    res += len(A_list[:bi_idx])

print(res)