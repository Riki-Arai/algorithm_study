'''
(1) BFSとして解こうとしたが、途中で保険加入者が含まれる場合にどうすればいいかわからず
(2) (1)の場合はより距離が長いものを採用する形で対処したがWA
(3) 原因分析に1時間以上かかったが、探索しきったあとに新たな保険加入者の距離が非常に長いときに探索索できない
(4) なので最終的にダイクストラ法に落ち着いたが、重みを持つ場合はダイクストラ法を検討した方がいいことを学んだ
(5) しかもDPの問題だったので、そもそも難しい解き方をしていたっぽい
    →グラフでもDPの可能性を捨てないようにしたいが、今回d問題ではその発想もなかった
'''
from collections import defaultdict
import heapq

N, M = map(int, input().split())

P_list = list(map(int, input().split()))

g_lists = [[] for _ in range(N + 1)]
for i, p in enumerate(P_list, 2):
    g_lists[p].append(i)

x2y_dict = defaultdict(int)
for _ in range(M):
    x, y = map(int, input().split())
    x2y_dict[x] = max(y, x2y_dict[x])

# 各ノードについて、現在わかっている最大のdis
seen_set = [-1] * (N + 1)

# (-dis, ノード) の順で管理
dq = []

for x, y in x2y_dict.items():
    seen_set[x] = y
    heapq.heappush(dq, (-y, x))

res_set = set()

while dq:
    neg_dis, a = heapq.heappop(dq)
    dis = -neg_dis

    # 古い情報ならスキップ
    if dis < seen_set[a]:
        continue

    res_set.add(a)

    if dis == 0:
        continue

    for b in g_lists[a]:
        new_dis = dis - 1

        # bに既に伝わっているdisより大きい場合だけ更新
        if new_dis > seen_set[b]:
            seen_set[b] = new_dis
            heapq.heappush(dq, (-new_dis, b))

print(len(res_set))