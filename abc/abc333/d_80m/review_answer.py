from collections import deque

N = int(input())
G = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visited = [False] * (N + 1)
visited[1] = True

max_size = 0

for s in G[1]:
    if visited[s]:
        continue

    q = deque([s])
    visited[s] = True
    size = 0

    while q:
        u = q.popleft()
        size += 1
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

    max_size = max(max_size, size)

print(N - max_size)