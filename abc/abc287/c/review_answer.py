import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU

N, M = map(int, input().split())

du = DSU(N)
g_list = [0] * (N+1)
for _ in range(M):
    a, b = list(map(int, input().split()))
    du.merge(a-1, b-1)
    g_list[a] += 1
    g_list[b] += 1

# パスグラフであればpathが1つのものが2つある
if du.size(0) == N and g_list.count(1) == 2 and g_list.count(2) == N-2:
    print("Yes")
else:
    print("No")