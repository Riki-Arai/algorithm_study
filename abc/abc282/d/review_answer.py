# 連結している部分グラフ内で同じ色を持つ点を連結してしまうと条件を満たさないことがポイントなので、枝になりうる数-M-条件を満たさない数で答えが求められる
import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

def f(n):
    return n*(n-1)//2

grid_lists = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    grid_lists[u].append(v)
    grid_lists[v].append(u)

is_bipartite = True
color_list = [-1]*(N+1)
dq = deque()
ng = 0
for i in range(1, N):
    if color_list[i] != -1:
        continue
    # 部分グラフの頂点の色を数える
    w_num, b_num = 0, 0
    dq.append(i)
    # ひとまず白にしてしまう
    color_list[i] = 0
    while len(dq):
        u = dq.popleft()
        if color_list[u] == 0:
            w_num += 1
        elif color_list[u] == 1:
            b_num += 1

        for v in grid_lists[u]:
            if color_list[v] != -1:
                # 部分グラフ内でも二部グラフの条件を満たさない時は、全体としても二部グラフとはいえなくなる
                # よって追加以前に問題文の条件を満たさなくなるのでFalseに変更し、答えも0が確定
                if color_list[u] == color_list[v]:
                    is_bipartite = False
            else:
                # 連結同士で同じ色であってはいけないので色を反転
                color_list[v] = 1 - color_list[u]
                dq.append(v)

    # 部分グラフ内で同じ色同士の頂点をペアにできないのでそれを数えあげる
    ng += f(w_num)+f(b_num)

if is_bipartite:
    print(f(N)-M-ng)
else:
    print(0)