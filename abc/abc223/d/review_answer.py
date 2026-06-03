import heapq

N, M = map(int, input().split())

f_g_lists = [set() for _ in range(N+1)]
b_g_lists = [set() for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    f_g_lists[A].add(B)
    b_g_lists[B].add(A)

q_list = []
for i in range(1, N+1):
    if len(b_g_lists[i]) == 0:
        q_list.append(i)

res_list = []
heapq.heapify(q_list)
while len(q_list) > 0:
    n = heapq.heappop(q_list)
    res_list.append(n)
    for nn in f_g_lists[n]:
        if len(b_g_lists[nn]) > 0:
            b_g_lists[nn].discard(n)
            if len(b_g_lists[nn]) == 0:
                heapq.heappush(q_list, nn)

if len(res_list) == N:
    print(*res_list)
else:
    print(-1)