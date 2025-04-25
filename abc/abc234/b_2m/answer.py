import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て

N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
for a_list in A_lists:
    for b_list in A_lists:
        if a_list != b_list:
            x, y = a_list
            xx, yy = b_list
            res = max(res, math.sqrt(pow(abs(x-xx), 2) + pow(abs(y-yy), 2)))

print(res)
