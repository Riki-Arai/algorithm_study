'''
(1) cの先にもdやeなどの頂点と接続している場合で、a→cのパスを追加するとa→dや→eといったパスを追加できることがわかった
(2) パスを追加したときに何か影響が出ていないかも考察してみたが問題がないことを確認
(3) 以上を踏まえてある頂点を起点として2以上の距離がある頂点の数をカウントする問題へと着地
(4) 頂点の数が小さいのでそれぞれの頂点を起点としたBFSでも時間的に間に合う
'''
import sys
from collections import deque
sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split()) # 取得例：1 2
    g_lists[u].append(v)

res = 0
for n in range(1, N+1):
    dq = deque([(n, 0)])
    seen_set = set([n])
    while len(dq):
        u, dis = dq.popleft()
        if dis >= 2:
            res += 1
        for v in g_lists[u]:
            if v not in seen_set:
                seen_set.add(v)
                dq.append((v, dis+1))

print(res)
