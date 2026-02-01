# setやdictのアクセスの平均計算量こそはO(1)だが、listのアクセスと比較して遅いためにTLEに繋げてしまった
# 一方でsetやdictの片方のみの利用であればギリギリACできたが、計算量がギリギリの時はまずはlistを使うことを念頭においた方が今後はいいかも
import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN
from collections import Counter, deque
from sys import setrecursionlimit
setrecursionlimit(10**7)

N, M = map(int, input().split())

g_list = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    g_list[a].append((b, c))
    g_list[b].append((a, c))

res = 0
tmp_res = 0

def dfs(n, c):
    global tmp_res, res
    for (next_t, next_c) in g_list[n]:
        if not seen_list[next_t]:
            seen_list[next_t] = True
            tmp_res += next_c
            res = max(res, tmp_res)
            dfs(next_t, next_c)

    tmp_res -= c
    seen_list[n] = False

for start_node in range(1, N+1):
    seen_list = [False] * (N+1)
    seen_list[start_node] = True
    tmp_res = 0
    dfs(start_node, 0)

print(res)

## 以下はNG
#import math, itertools, bisect, functools, copy, decimal
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from collections import defaultdict, Counter, deque
#
#N, M = map(int, input().split())
#
#grid_dict = defaultdict(set)
#w_dict = defaultdict(int)
#for _ in range(M):
#    A, B, C = map(int, input().split())
#    grid_dict[A].add(B)
#    grid_dict[B].add(A)
#    w_dict[(A, B)] = C
#    w_dict[(B, A)] = C
#
#def dfs(e):
#    if grid_list[e]:
#        return True
#    grid_list[e] = True
#    e_set = grid_dict[e]
#    for ee in e_set:
#        if dfs(ee):
#            continue
#        tmp_list.append(w_dict[(e, ee)])
#
#res = 0
#for i in range(1, N+1):
#    tmp_list = []
#    grid_list = [False] * (N+1)
#    if dfs(i):
#        continue
#    res = max(sum(tmp_list), res)
#
#print(res)