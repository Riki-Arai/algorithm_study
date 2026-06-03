N, M = map(int, input().split())

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    g_lists[a].append(b)
