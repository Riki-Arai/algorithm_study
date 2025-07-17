import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

K = int(input())

res_list = []
n_list = [str(i) for i in range(10)]
p_lists = list(itertools.product([0, 1], repeat=10))
for p_list in p_lists:
    tmp_list = []
    for i, p in enumerate(p_list):
        if p == 1:
            tmp_list.append(n_list[i])

    tmp_list.sort(reverse=True)
    if "".join(tmp_list) != "":
        res_list.append(int("".join(tmp_list)))

res_list.sort()
print(res_list[K])