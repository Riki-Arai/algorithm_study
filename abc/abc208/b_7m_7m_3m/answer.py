import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て

P = int(input())

res = 0
for n in range(10, 0, -1):
    m = math.factorial(n)
    for i in range(100, 0, -1):
        if m*i <= P:
            res += i
            P -= m*i
            break

    if P == 0:
        print(res)
        break
