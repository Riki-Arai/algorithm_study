# 2つに分割する、つまり2つのグループに分けて数字列を作ればいいのでbit全探索が使える
# 桁数も9桁なので計算量も問題がない(512ほどくらい)
import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

N = int(input())

res = 0
str_n = str(N)
p_lists = list(itertools.product([0, 1], repeat=len(str(N))))
for p_list in p_lists:
    a_list, b_list = [], []
    for i, p in enumerate(p_list):
        if p == 1:
            a_list.append(str_n[i])
        else:
            b_list.append(str_n[i])

    a_list.sort(reverse=True) # 0が前にならないようにする
    b_list.sort(reverse=True)
    if len(a_list) > 0 and len(b_list) > 0 and not(a_list[0] == 0 or b_list[0] == 0):
        res = max(int("".join(a_list)) * int("".join(b_list)), res)

print(res)