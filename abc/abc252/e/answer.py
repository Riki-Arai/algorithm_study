'''
(1) コストを最小に抑えるパスということでダイクストラ法を採用すると良さそう
(2) 考察はすぐにできたが実装方法を正しく理解していないために時間がかかりすぎた
'''
import heapq as hq

N, M = map(int, input().split()) # 取得例：1 2

g_lists = [[] for _ in range(N+1)]
for i in range(1, M+1):
    A, B, C = map(int, input().split()) # 取得例：1 2
    g_lists[A].append((B, C, i))
    g_lists[B].append((A, C, i))

res_list = []
c_list = [float("INF")]*(N+1)
c_list[1] = 0
hq_lists = [(0, 1, None)]
hq.heapify(hq_lists)
while len(hq_lists):
    c, u, r = hq.heappop(hq_lists)
    if c > c_list[u]:
        continue

    if r != None:
        res_list.append(r)

    for v, cc, i in g_lists[u]:
        if c_list[v] > c+cc:
            c_list[v] = c+cc
            hq.heappush(hq_lists, (c+cc, v, i))

print(*res_list)


hq_list = [(0, 1)]
hq.heapify(hq_list)
res_list = [float("inf")] * (N + 1)
res_list[1] = 0
while hq_list:
    w, u = hq.heappop(hq_list)
    if w > res_list[u]:
        continue

    for v, b in g_lists[u]:
        ww = w + b
        if res_list[v] > ww:
            res_list[v] = ww
            hq.heappush(hq_list, (ww, v))