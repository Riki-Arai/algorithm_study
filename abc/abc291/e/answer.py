import heapq as hq


N, M = map(int, input().split()) # 取得例：1 2

g_lists = [[] for _ in range(N+1)]
oe_list = [0]*(N+1)
seen_sets = set()
for _ in range(M):
    X, Y = map(int, input().split()) # 取得例：1 2
    if (X, Y) not in seen_sets:
        g_lists[Y].append(X)
        oe_list[X] += 1
        seen_sets.add((X, Y))

hq_list = []
hq.heapify(hq_list)
res_list = [0]*(N+1)
for n in range(1, N+1):
    if not oe_list[n]:
        hq.heappush(hq_list, n)

v = N
while len(hq_list):
    if len(hq_list) >= 2:
        print("No")
        exit()

    n = hq.heappop(hq_list)
    res_list[n] = v
    v -= 1
    for nn in g_lists[n]:
        oe_list[nn] -= 1
        if oe_list[nn] == 0:
            hq.heappush(hq_list, nn)

print("Yes")
print(*res_list[1:])