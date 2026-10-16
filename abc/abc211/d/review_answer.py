from collections import deque

N, M = map(int, input().split())

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    g_lists[A].append(B)
    g_lists[B].append(A)

MOD = 10**9+7
dq = deque()
dq.append((1, 0))
dis_list = [float("INF")]*(N+1)
dis_list[1] = 0
way_list = [0]*(N+1)
way_list[1] = 1
while len(dq):
    a, dis = dq.popleft()
    for b in g_lists[a]:
        if dis+1 == dis_list[b]:
            way_list[b] = (way_list[a]+way_list[b])%MOD
        elif dis+1 < dis_list[b]:
            dis_list[b] = dis+1
            way_list[b] = way_list[a]%MOD
            dq.append((b, dis+1))

print(way_list[N]%MOD)