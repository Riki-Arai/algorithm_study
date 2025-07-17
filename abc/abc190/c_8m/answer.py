import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
B_lists = [list(map(int, input().split())) for _ in range(K)]

res = 0
p_lists = list(itertools.product(*B_lists))
for p in p_lists:
    p_set = set(p)
    count = 0
    for A_list in A_lists:
        a, b = A_list
        if a in p_set and b in p_set:
            count += 1

    res = max(count, res)

print(res)