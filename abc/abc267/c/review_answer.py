# 途中の区間の累積和の求め方を学んだ
import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
A_list = list(map(int, input().split()))

partial_A = [0] * (N + 1)
for i in range(N):
    partial_A[i + 1] = partial_A[i] + A_list[i]

current = 0
for i in range(M):
    current += (i + 1) * A_list[i]

ans = current
for start in range(N - M):
    # startからMまでの区間の累積和を求めることができる
    old_sum = partial_A[start + M] - partial_A[start]
    current = current - old_sum + M * A_list[start + M]
    ans = max(ans, current)

print(ans)