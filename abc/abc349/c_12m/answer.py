import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

S = input().strip()
T = input().strip()

T = T.lower()
idx = 0
if T[-1] == "x":
    for s in S:
        if s == T[idx]:
            idx += 1
        if idx == 2:
            print("Yes")
            exit()
    print("No")
else:
    for s in S:
        if s == T[idx]:
            idx += 1
        if idx == 3:
            print("Yes")
            exit()
    print("No")