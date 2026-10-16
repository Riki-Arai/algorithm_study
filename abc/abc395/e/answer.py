import heapq

N, M, X = map(int, input().split())

normal = [[] for _ in range(N)]
reverse = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    normal[u].append(v)
    reverse[v].append(u)

INF = float("inf")

# dist[v][state]
# state = 0: 通常
# state = 1: 反転
dist = [[INF] * 2 for _ in range(N)]

dist[0][0] = 0

pq = [(0, 0, 0)]  # (距離, 頂点, 状態)

while pq:
    d, v, state = heapq.heappop(pq)

    if d > dist[v][state]:
        continue

    # 今の状態の向きで進む
    if state == 0:
        graph = normal
    else:
        graph = reverse

    for nv in graph[v]:
        nd = d + 1

        if nd < dist[nv][state]:
            dist[nv][state] = nd
            heapq.heappush(pq, (nd, nv, state))

    # 向きを反転する
    if d + X < dist[v][1 - state]:
        dist[v][1 - state] = d + X
        heapq.heappush(pq, (d + X, v, 1 - state))

print(min(dist[N - 1]))