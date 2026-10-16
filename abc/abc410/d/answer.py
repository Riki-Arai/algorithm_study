import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2

g_lists = [[] for _ in range(N+1)]
e2w_lists = [[None]*(N+1) for _ in range(N+1)]
for _ in range(M):
    A, B, W = map(int, input().split()) # 取得例：1 2
    g_lists[A].append(B)
    e2w_lists[A][B] = W

res = float("INF")
e2c_lists = [[0]*(N+1) for _ in range(N+1)]
def dfs(u, w):
    global res
    for v in g_lists[u]:
        if e2c_lists[u][v] < 2:
            e2c_lists[u][v] += 1
            if v == N:
                res = min(w^e2w_lists[u][v], res)
            dfs(v, w^e2w_lists[u][v])
            e2c_lists[u][v] -= 1

dfs(1, 0)
if res == float("INF"):
    print(-1)
else:
    print(res)