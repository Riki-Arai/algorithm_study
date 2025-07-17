import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

N, K = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

count = 0
sum_ = 0
dq = deque()
for i in range(N):
    dq.append(A_list[i])
    sum_ += A_list[i]
    while len(dq) and sum_ >= K:
        dq.popleft()
    count += len(dq)

print(2**N-count)