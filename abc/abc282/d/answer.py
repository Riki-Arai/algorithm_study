from collections import deque

N, M = map(int, input().split())

grid_lists = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    grid_lists[u].append(v)
    grid_lists[v].append(u)