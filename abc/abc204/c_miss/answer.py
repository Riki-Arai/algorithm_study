import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

g_lists = [[] for _ in range(N+1)]
for a, b in A_lists:
    g_lists[a].append(b)