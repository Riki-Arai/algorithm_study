import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

N, K = map(int, input().split())
C_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
res_dict = defaultdict(int)
res_set = set()
dq = deque()
for i in range(N):
    dq.append(C_list[i])
    res_set.add(C_list[i])
    res_dict[C_list[i]] += 1
    while len(dq) and len(dq) > K:
        l = dq.popleft()
        res_dict[l] -= 1
        if res_dict[l] == 0:
            res_set.discard(l)

    res = max(len(res_set), res)

print(res)