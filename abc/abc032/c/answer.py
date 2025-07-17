import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

N, K = map(int, input().split()) # 取得例：1 2

s_list = []
for _ in range(N):
    n = int(input().strip())
    s_list.append(n)

if 0 in s_list:
    print(len(s_list))
    exit()

res = 0
mul = 1
dq = deque()
for i in range(N):
    dq.append(s_list[i])
    mul *= s_list[i]
    while len(dq) >= 1 and not mul <= K:
        mul /= dq.popleft()
    res = max(len(dq), res)

print(res)