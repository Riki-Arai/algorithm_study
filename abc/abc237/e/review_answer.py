'''
※ACできず
(1) 嬉しさが結局は始点と終点の高さによって決まる点を発見できたまでは良かった。
(2) 嬉しさの最大化に躍起になってしまったが、コストを最低にする問題とも言い換える視点を持つべきだった。改めて反対の視点を持つ大切さを学んだ。
(3) ポテンシャル法によって重みを全て正にする視点も持つ大事さを学べた
(4) 意外と解説に納得いくまでに時間がかかったのでもっと早く解答をみるべきだったか。。。
'''
import heapq as hq

N, M = map(int, input().split()) # 取得例：1 2
H_list =  list(map(int, input().split()))

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    U, V = map(int, input().split()) # 取得例：1 2
    if H_list[V-1] > H_list[U-1]:
        g_lists[U].append((H_list[V-1]-H_list[U-1], V))
        g_lists[V].append((0, U))
    elif H_list[V-1] < H_list[U-1]:
        g_lists[U].append((0, V))
        g_lists[V].append((H_list[U-1]-H_list[V-1], U))
    else:
        g_lists[U].append((0, V))
        g_lists[V].append((0, U))

hq_list = [(0, 1)]
hq.heapify(hq_list)
res_list = [float("inf")] * (N + 1)
res_list[1] = 0
while hq_list:
    w, u = hq.heappop(hq_list)
    if w > res_list[u]:
        continue

    for b, v in g_lists[u]:
        ww = w + b
        if res_list[v] > ww:
            res_list[v] = ww
            hq.heappush(hq_list, (ww, v))

res = 0
for i, c in enumerate(res_list[1:]):
    if c != float("INF"):
        res = max(H_list[0]-H_list[i]-c, res)

print(res)