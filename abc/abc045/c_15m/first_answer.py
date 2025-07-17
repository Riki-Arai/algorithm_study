import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て

S_list = list(input().strip()) # 取得例："A"

res_set = set()
p_lists = list(itertools.product([0, 1], repeat=len(S_list)))
for p_list in p_lists:
    tmp_s_list = S_list[:]
    insert_idx = 0
    for i, p in enumerate(p_list):
        if p == 1 and i != 0:
            tmp_s_list.insert(i + insert_idx, "+")
            insert_idx += 1

    res_set.add("".join(tmp_s_list))

sum_ = 0
for res in res_set:
    res_list = res.split("+")
    sum_ += sum(list(map(int, res_list)))

print(sum_)