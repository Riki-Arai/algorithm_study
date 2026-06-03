from collections import deque

N, M = map(int, input().split())
g_lists = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    g_lists[A].append(B)
    g_lists[B].append(A)

INF = 10**9+7
dq = deque()
dis_list = [0]*(N+1)
res_list = [0]*(N+1)
seen_set = set()
dq.append(1)
seen_set.add(1)
dis_list[1] = 0
res_list[1] = 1
while len(dq):
    a = dq.popleft()
    for b in g_lists[a]:
        if b in seen_set:
            if dis_list[b] == dis_list[a] + 1:
                res_list[b] = (res_list[b] + res_list[a])%INF
        else:
            seen_set.add(b)
            dis_list[b] = dis_list[a] + 1
            res_list[b] = res_list[a]%INF
            dq.append(b)

print(res_list[N])



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