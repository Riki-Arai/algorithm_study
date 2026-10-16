import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    dist = [-1] * N
    dist[start] = 0

    q = deque([start])

    while q:
        v = q.popleft()

        for nv in graph[v]:
            if dist[nv] != -1:
                continue

            dist[nv] = dist[v] + 1
            q.append(nv)

    # 距離が最大、同距離なら頂点番号が最大
    farthest = 0
    for v in range(N):
        if dist[v] > dist[farthest]:
            farthest = v
        elif dist[v] == dist[farthest] and v > farthest:
            farthest = v

    return farthest, dist


# (1)
u, _ = bfs(0)

# (2)
v, dist_u = bfs(u)

# (3)
_, dist_v = bfs(v)

# (4)
# 各頂点 x から最も遠い頂点を、
# dist_u[x] と dist_v[x] の大きい方から選ぶ。
# 同じなら頂点番号が大きい方。
ans = []

for x in range(N):
    if dist_u[x] > dist_v[x]:
        ans.append(u + 1)
    elif dist_u[x] < dist_v[x]:
        ans.append(v + 1)
    else:
        ans.append(max(u, v) + 1)

print(*ans, sep="\n")
