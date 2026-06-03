import sys; sys.setrecursionlimit(10**7)

N, M, L, S, T = map(int, input().split()) # 取得例：1 2
g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    U, V, C = map(int, input().split()) # 取得例：1 2
    g_lists[U].append((V, C))

res_set = set()
def dfs(u, w, d):
    for v, c in g_lists[u]:
        if d+1 == L:
            if S <= w+c <= T:
                res_set.add(v)
        else:
            dfs(v, w+c, d+1)

dfs(1, 0, 0)
print(*sorted(list(res_set)))