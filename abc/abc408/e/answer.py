import sys; sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2

g_lists = [[] for _ in range(N+1)]
e_list = 
for _ in range(M):
    u, v, w = map(int, input().split()) # 取得例：1 2
    g_lists[u].append((v, w))
    g_lists[v].append((u, w))

res = float("INF")
seen_set = set([1])
def dfs(u, tmp_res):
    global res
    for v, w in g_lists[u]:
        if v == N:
            res = min(tmp_res|w, res)
            continue
        if v not in seen_set:
            seen_set.add(v)
            dfs(v, tmp_res|w)

dfs(1, 0)
print(res)