import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    g_lists[u].append([v, w])
    g_lists[v].append([u, w])

res = float("INF")
seen_set = set()
def dfs(n, tmp_res):
    global res
    seen_set.add(n)
    for nn, w in g_lists[n]:
        if nn == N:
            res = min(tmp_res^w, res)
            continue
        if nn not in seen_set:
            seen_set.add(nn)
            dfs(nn, tmp_res^w)
            seen_set.discard(nn)

    seen_set.discard(n)

dfs(1, 0)
print(res)