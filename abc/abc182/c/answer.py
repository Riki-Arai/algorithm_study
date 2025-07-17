import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

N = int(input()) # 取得例：1

res = float("INF")
p_lists = list(itertools.product([0, 1], repeat=len(str(N))))
for p_list in p_lists:
    tmp_list = []
    for i, p in enumerate(p_list):
        if p == 1:
            tmp_list.append(str(N)[i])

    if len(tmp_list) > 0:
        tmp_res = int("".join(tmp_list))
        if tmp_res % 3 == 0:
            res = min(len(str(N)) - len(tmp_list), res)

if res == float("INF"):
    print(-1)
else:
    print(res)