from collections import deque

N, M = map(int, input().split())

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    g_lists[A].append(B)
    g_lists[B].append(A)

MOD = (10**9+7)
dq = deque()
dq.append(1)
seen_set = set()
seen_set.add(1)
dis_list = [float("INF")]*(N+1)
dis_list[1] = 0
way_list = [0]*(N+1)
way_list[1] = 1
while len(dq):
    a = dq.popleft()
    d = dis_list[a]
    w = way_list[a]
    for b in g_lists[a]:
        if b not in seen_set:
            way_list[b] = w%MOD
            dis_list[b] = d + 1
            seen_set.add(b)
            dq.append(b)
        elif b in seen_set and dis_list[b] == d + 1:
            way_list[b] = (way_list[b] + w)%MOD

print(way_list[N]%MOD)