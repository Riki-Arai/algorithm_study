import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て

N, M, X = map(int, input().split()) # 取得例：1 2
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = float("INF")
p_lists = list(itertools.product([0, 1], repeat=N))
for p_list in p_lists:
    tmp_res = 0
    res_list = [0] * M
    for i, p in enumerate(p_list):
        if p == 1:
            tmp_res += A_lists[i][0]
            for j in range(M):
                res_list[j] += A_lists[i][j+1]

    if all(list(map(lambda x: x >= X, res_list))):
        res = min(tmp_res, res)

if res == float("INF"):
    print(-1)
else:
    print(res)