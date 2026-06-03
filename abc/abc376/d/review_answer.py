from collections import defaultdict, Counter, deque

N, M = map(int, input().split())

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    g_lists[a].append(b)

seen_set = set()
seen_set.add(1)
dq = deque()
dq.append(1)
dis_list = [0]*(N+1)
res = float("INF")
while len(dq):
    a = dq.popleft()
    dis = dis_list[a]
    for b in g_lists[a]:
        if b == 1:
            res = min(dis+1, res)
        elif b not in seen_set:
            seen_set.add(b)
            dis_list[b] = dis + 1
            dq.append(b)

if res == float("INF"):
    print(-1)
else:
    print(res)