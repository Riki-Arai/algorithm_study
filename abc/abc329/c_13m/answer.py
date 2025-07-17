import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

N = int(input())
S = input().strip()

alp_dict = {chr(i):0 for i in range(ord('a'), ord('z') + 1)}
for k, v in itertools.groupby(list(S)):
    v_list = list(v)
    alp_dict[k] = max(alp_dict[k], len(v_list))

res = 0
for k, v in alp_dict.items():
    res += v

print(res)