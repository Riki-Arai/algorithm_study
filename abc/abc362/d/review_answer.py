import heapq as hq

N, M = map(int, input().split())
A_list = list(map(int, input().split()))

g_lists = [[] for _ in range(N + 1)]

for _ in range(M):
    U, V, B = map(int, input().split())

    # U -> V に移動するときは、辺 B + 頂点 V の重み
    g_lists[U].append((V, B + A_list[V - 1]))

    # V -> U に移動するときは、辺 B + 頂点 U の重み
    g_lists[V].append((U, B + A_list[U - 1]))

move_lists = [(A_list[0], 1)]
res_list = [float("inf")] * (N + 1)
res_list[1] = A_list[0]

while move_lists:
    w, u = hq.heappop(move_lists)

    if w > res_list[u]:
        continue

    for v, b in g_lists[u]:
        ww = w + b

        if res_list[v] > ww:
            res_list[v] = ww
            hq.heappush(move_lists, (ww, v))

print(*res_list[2:])