from collections import defaultdict, Counter, deque

N, M = map(int, input().split())

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, X, Y = map(int, input().split())
    g_lists[A].append([B, X, Y])
    g_lists[B].append((A, -X, -Y))

res_lists = [[] for _ in range(N+1)]
seen_set = set()
dq = deque()
seen_set.add(1)
dq.append(1)
res_lists[1].append((0, 0))
while len(dq):
    n = dq.popleft()
    x, y = res_lists[n][0]
    for nn, mx, my in g_lists[n]:
        if nn not in seen_set:
            seen_set.add(nn)
            res_lists[nn].append((x+mx, y+my))
            dq.append(nn)

for i in range(1, N+1):
    if len(res_lists[i]):
        x, y = res_lists[i][0]
        print(x, y)
    else:
        print("undecidable")