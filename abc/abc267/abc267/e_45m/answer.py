'''
(1) 処理時間が4秒以内と大きく、重みの合計が多いものを削除してしまうと最大値が大きくなってしまう
(2) そのため単純に重みの合計が少ないものから順番に削除をする方法はどうか？
(3) 頂点を削除をする際に他の頂点の重みを更新して優先度付きキューに入れる方針でも間に合いそう(N*Mくらいのイメージ)
(4) 検証に時間がかかったが方針に問題がなさそうだったのであとは実装をするだけ
'''
import heapq as hq

N, M = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

g_lists = [[] for _ in range(N+1)]
w_list = [0]*(N+1)
for _ in range(M):
    U, V = map(int, input().split()) # 取得例：1 2
    g_lists[U].append(V)
    g_lists[V].append(U)
    w_list[U] += A_list[V-1]
    w_list[V] += A_list[U-1]

hq_lists = []
for i, w in enumerate(w_list[1:], 1):
    hq_lists.append((w, i))

res = 0
seen_set = set()
hq.heapify(hq_lists)
while len(hq_lists):
    w, u = hq.heappop(hq_lists)
    if u in seen_set:
        continue

    sum_ = 0
    seen_set.add(u)
    for v in g_lists[u]:
        if v not in seen_set:
            sum_ += A_list[v-1]
            w_list[v] -= A_list[u-1]
            if w_list[v] > 0:
                hq.heappush(hq_lists, (w_list[v], v))

    res = max(sum_, res)

print(res)