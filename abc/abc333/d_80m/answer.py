from atcoder.dsu import DSU
from collections import deque

N = int(input())

grid_lists = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    grid_lists[u].append(v)
    grid_lists[v].append(u)

seen_set = set()
seen_set.add(1)
dq = deque()
for v in grid_lists[1]:
    dq.append(v)
    seen_set.add(v)

dsu = DSU(N)
while len(dq):
    u = dq.popleft()
    for v in grid_lists[u]:
        if v not in seen_set:
            dq.append(v)
            seen_set.add(v)
            dsu.merge(u-1, v-1)

n_list = []
for g in dsu.groups():
    if g[0] != 0:
        n_list.append(len(g))

res = 0
n_list.sort()
for n in n_list[:-1]:
    res += n

print(res+1)