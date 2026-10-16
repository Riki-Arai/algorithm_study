N, M = map(int, input().split())

for _ in range(M):
    A, B = map(int, input().split())
    g_lists[A].append(B)
    ig_list[B] += 1

dq_list = []
hq.heapify(dq_list)
for i in range(1, N+1):
    if ig_list[i] == 0:
        hq.heappush(dq_list, i)

res_list = []
while len(dq_list):
    n = hq.heappop(dq_list)
    res_list.append(n)
    for nn in g_lists[n]:
        ig_list[nn] -= 1
        if ig_list[nn] == 0:
            hq.heappush(dq_list, nn)

if len(res_list) == N:
    print(*res_list)
else:
    print(-1)