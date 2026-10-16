# leaderを使って代表の数字にマッピングして頂点と枝の数をカウントしていくイメージ
import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

input_data = sys.stdin.read().strip().split()
N, M = map(int, input_data[:2])

dsu = DSU(N)

edges = []
idx = 2
for _ in range(M):
    u = int(input_data[idx]);   idx += 1
    v = int(input_data[idx]);   idx += 1
    u -= 1
    v -= 1
    edges.append((u, v))
    dsu.merge(u, v)

vs = [0]*N
es = [0]*N
for i in range(N):
    vs[dsu.leader(i)] += 1

for (u, v) in edges:
    r = dsu.leader(u)  # u, vの頂点は同じ
    es[r] += 1 # 頂点にマッピングして枝数をカウント（入力1の(2, 3)のケースでも合計2個の数え上げができる）

if vs == es:
    print("Yes")
else:
    print("No")