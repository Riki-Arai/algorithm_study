from collections import deque
MOD = 10**9 + 7

N, M = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

dist = [-1] * (N + 1)
ways = [0] * (N + 1)
dist[1] = 0
ways[1] = 1
dq = deque([1])
while dq:
    u = dq.popleft()
    for v in g[u]:
        # 最初に最短経路に到達する時にdistとwaysの記録をとる
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            ways[v] = ways[u]
            dq.append(v)
        # dist[u]+1=dist[v]であれば最短経路に到達したと判断できる
        elif dist[v] == dist[u] + 1:      # 同じ最短距離での到達を加算
            ways[v] = (ways[v] + ways[u]) % MOD

print(ways[N] % MOD)