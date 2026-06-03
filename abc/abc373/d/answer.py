N, M = map(int, input().split())

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())