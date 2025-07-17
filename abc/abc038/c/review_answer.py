import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

N = int(input()) # 数値：1
A_list = list(map(int, input().split()))

res = 0
dq = deque()
for i in range(N):
    dq.append(A_list[i])
    # 最初はdq[0] < dq[-1]のようなことをしていたが、for文と同じような感覚で常に新しくappendした時の値と比較する
    while len(dq) >= 2 and not (dq[-2] < dq[-1]):
        dq.popleft()
    # 重複した数え上げにみえるが、dqに1,2,3,4とあれば(1,4),(2,4),(3,4),(4)を数え上げるイメージであり、dqの長さと一致する。
    res += len(dq)

print(res)