import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て

N = int(input().strip())
A_list = list(map(int, input().split()))

res = float("INF")
for bit in itertools.product([0, 1], repeat=N):
    a_time, b_time = 0, 0
    for i, x in enumerate(bit):
        if x == 1:
            a_time += A_list[i]
        else:
            b_time += A_list[i]
    res = min(max(a_time, b_time), res)

print(res)