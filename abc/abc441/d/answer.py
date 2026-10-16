import sys; sys.setrecursionlimit(10**7)

N, M, L, S, T = map(int, input().split()) # 取得例：1 2
g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    U, V, C = map(int, input().split()) # 取得例：1 2
    g_lists[U].append((V, C))

res_set = set()
def dfs(u, w, l):
    if l == L and S <= w <= T:
        res_set.add(u)
        return
    elif l == L and not(S <= w <= T):
        return

    for v, c in g_lists[u]:
        if l+1 <= L:
            dfs(v, w+c, l+1)

dfs(1, 0, 0)
print(*sorted(list(res_set)))