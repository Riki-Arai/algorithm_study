import sys; sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split()) # 取得例：1 2
    g_lists[u].append(v)
    g_lists[v].append(u)

INF = 10**6
res = 0
seen_set = set()
def dfs(u):
    global res
    seen_set.add(u)
    res += 1
    if res == INF:
        print(res)
        exit()

    for v in g_lists[u]:
        if v not in seen_set:
            dfs(v)
    seen_set.discard(u)

dfs(1)
print(min(res, INF))