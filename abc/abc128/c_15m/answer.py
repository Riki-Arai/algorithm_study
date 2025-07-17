import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

N, M = map(int, input().split()) # 取得例：1 2
s_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]
x_list = list(map(int, input().split()))

res = 0
p_lists = list(itertools.product([0, 1], repeat=N))
for p_list in p_lists:
    tmp_res = 0
    for i, s_list in enumerate(s_lists):
        count = 0
        for s in s_list[1:]:
            if p_list[s-1] == 1:
                count += 1

        if count % 2 == x_list[i]:
            tmp_res += 1

    if tmp_res == M:
        res += 1

print(res)