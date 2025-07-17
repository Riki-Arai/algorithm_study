import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

N, K = map(int, input().split())
S_list = [input() for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用

res = 0
p_lists = list(itertools.product([0, 1], repeat=N))
for p_list in p_lists:
    tmp_res = 0
    tmp_list = []
    for i, p in enumerate(p_list):
        if p == 1:
            tmp_list.extend(list(S_list[i]))

    c = Counter(tmp_list)
    for k, v in c.items():
        if v == K:
            tmp_res += 1

    res = max(tmp_res, res)

print(res)
