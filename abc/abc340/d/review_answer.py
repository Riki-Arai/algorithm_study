import heapq as hq

N = int(input())

g_lists = [[] for _ in range(N+1)]
for i in range(1, N):
    A, B, X = map(int, input().split())
    g_lists[i].append((A, i+1))
    g_lists[i].append((B, X))

res_list = [float("INF")]*(N+1)
res_list[1] = 0
res_lists = [(0, 1)]
hq.heapify(res_lists)
while len(res_lists):
    c, n = hq.heappop(res_lists)
    '''
    ・362_Dの解説を確認した後に追加。
    ・条件次第でnにとって現時点で最適なcをres_listに格納している可能性がある。
    ・この問題では枝が2つしかなかったのでACするが、362_Dでは枝が多い関係で無駄にfor文を回してTLEになってしまっていた
    '''
    if c > res_list[n]:
        continue

    for cc, nn in g_lists[n]:
        if c+cc < res_list[nn]:
            res_list[nn] = min(res_list[nn], c+cc)
            hq.heappush(res_lists, (c+cc, nn))

print(res_list[N])