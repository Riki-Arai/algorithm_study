import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

sum_ = 0
res_dict = defaultdict(int)
s_A_list = sorted(A_list)
for a in s_A_list:
    sum_ += a
    res_dict[a] = sum_

res_list = []
for a in A_list:
    res_list.append(sum_-res_dict[a])

print(*res_list)