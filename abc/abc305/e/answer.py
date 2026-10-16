'''
(1) それぞれの点からの距離に関する問題なので多視点BFSの出番だと予想
(2) 今回の設定だと警備員の体力が異なる
(3) 体力が大きい順に行動することが最適そうなので、ダイクストラ法のようなもので実装
(4) 最初は警備員がいる地点の更新をしていなかったが、冷静に考えたら最大を更新する可能性があることに気づいた（それでWAをした）
'''
import heapq as hq

N, M, K = map(int, input().split()) # 取得例：1 2

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split()) # 取得例：1 2
    g_lists[a].append(b)
    g_lists[b].append(a)

seen_set = set()
hq_lists = []
h_list = [0]*(N+1)
hq.heapify(hq_lists)
for _ in range(K):
    p, h = map(int, input().split()) # 取得例：1 2
    hq.heappush(hq_lists, (-h, p))
    h_list[p] = h
    seen_set.add(p)

while hq_lists:
    h, u = hq.heappop(hq_lists)
    h *= -1
    if h_list[u] > h:
        continue

    for v in g_lists[u]:
        if h-1 == 0:
            seen_set.add(v)
        elif h-1 > h_list[v]:
            seen_set.add(v)
            h_list[v] = h-1
            hq.heappush(hq_lists, (-(h-1), v))
  
print(len(seen_set))
print(*sorted(list(seen_set)))