# 例題を見れば条件の意味を理解できるが、条件のみでも理解できるようにしておきたい
# 理解さえすれば難易度はそこまで高くはない
import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

N, M = map(int, input().split())
A_lists = []
for _ in range(M):
    c = int(input())
    A_lists.append(list(map(int, input().split())))

res = 0
res_set = set()
n_set = set(i for i in range(1, N+1))
p_lists = list(itertools.product([0, 1], repeat=M))
for p_list in p_lists:
    for i, p in enumerate(p_list):
        if p == 1:
            res_set |= set(A_lists[i])

    if res_set == n_set:
        res += 1

    res_set = set()

print(res)