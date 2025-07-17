N,M=map(int,input().split())
E=[[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    E[a][b]=c
    E[b][a]=c

ans=0
used=[False]*(N+1)
def dfs(v,s):
    global ans
    used[v]=True
    ans = max(s, ans)
    for i in range(1, N+1):
        if not used[i] and E[v][i]:
            dfs(i,s+E[v][i])
    used[v]=False

for i in range(1,N+1):
    dfs(i,0)

print(ans)

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