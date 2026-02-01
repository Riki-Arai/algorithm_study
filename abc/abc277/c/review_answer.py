# 20260124で解いた時のDFS
import sys, math, itertools as it, bisect as bi, functools as ft, copy, decimal, heapq as hq
from collections import defaultdict, Counter, deque
sys.setrecursionlimit(10**7)

N = int(input())

g_dict = defaultdict(set)
for _ in range(N):
    A, B = map(int, input().split())
    g_dict[A].add(B)
    g_dict[B].add(A)

res = 1
seen_set = set()
def dfs(a):
    global res
    for b in g_dict[a]:
        if b not in seen_set:
            res = max(b, res)
            seen_set.add(b)
            dfs(b)

dfs(1)
print(res)


# DSUを使う場合
import sys
from atcoder.dsu import DSU

input = sys.stdin.readline

N = int(input())

edges = []
values = set()

for _ in range(N):
    A, B = map(int, input().split())
    edges.append((A, B))
    values.add(A)
    values.add(B)

arr = sorted(values)
if arr[0] != 1:
    print(1)
    sys.exit()

index_map = {v: i for i, v in enumerate(arr)}
dsu = DSU(len(arr))
for A, B in edges:
    dsu.merge(index_map[A], index_map[B])

idx_of_1 = index_map[1]
for group in dsu.groups():
    if idx_of_1 in group:
        ladder_top = arr[max(group)]
        print(ladder_top)
        break


## ハシゴの行き来が可能であることが考慮していなかった。行き来が可能である場合は訪問済みであるかどうかの確認も必要。
#import sys, math, itertools, bisect, functools, copy, decimal
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from collections import defaultdict, Counter, deque
#from atcoder.dsu import DSU
#sys.setrecursionlimit(10**7)
#
#N = int(input())
#
#res_list = []
#res_dict = defaultdict(set)
#for _ in range(N):
#    A, B = map(int, input().split())
#    res_dict[A].add(B)
#    res_dict[B].add(A)
#
#res = 1
## リストを使うと要素数によってはTLEなどになるので、セットを利用して訪問済みであるかどうかを確認
#seen_set = set()
#def dfs(i):
#    global res
#    if i in seen_set or i not in res_dict:
#        return
#    seen_set.add(i)
#    next_f_set = res_dict[i]
#    for f in next_f_set:
#        res = max(f, res)
#        dfs(f)
#
#dfs(1)
#print(res)