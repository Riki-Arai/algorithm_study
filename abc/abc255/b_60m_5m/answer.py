import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て

N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
for B_list in B_lists:
    tmp_res = float("INF")
    x, y = B_list
    for a in A_list:
        xx, yy = B_lists[a-1]
        tmp_res = min(pow(abs(x-xx), 2) + pow(abs(y-yy), 2), tmp_res)

    res = max(tmp_res, res)

print(pow(res, 0.5))