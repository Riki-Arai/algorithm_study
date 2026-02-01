from collections import deque

N, M = map(int, input().split())
g_lists = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    g_lists[A].append(B)
    g_lists[B].append(A)

res = 0
way_list = [-1]*(N+1)
seen_set = set()
dq = deque()
dq.append(1)
way_list[1] = 1
seen_set.add(1)
while len(dq):
    a = dq.popleft()
    for b in g_lists[a]:
        if b not in seen_set:
            way_list[b] = (way_list[a])%(10**9+7)
            dq.append(b)
            seen_set.add(b)
        else:
            way_list[b] = (way_list[b] + way_list[a])%(10**9+7)

if way_list[N] != -1:
    print(way_list[N]%(10**9+7))
else:
    print(0)