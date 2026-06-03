# なるべく1つの点に対して初期値を決めて伝搬させる方法を考えることがポイントだった
# 有向グラフなので逆方向からも重み更新をできる枝を追加することで上記の条件を満たせる
from collections import deque

N, M = map(int, input().split())

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    g_lists[u].append([v, w])
    # この問題のキモとなる処理
    g_lists[v].append([u, -w])

seen_set = set()
res_list = [None]*(N+1)
# 連結成分が複数あるケースがあるのでforたた対応
for i in range(1, N+1):
    if i in seen_set:
        continue
    dq = deque()
    dq.append(i)
    seen_set.add(i)
    res_list[i] = 0
    while len(dq):
        u = dq.popleft()
        uw = res_list[u]
        for v, w in g_lists[u]:
            if v not in seen_set:
                seen_set.add(v)
                res_list[v] = uw + w
                dq.append(v)

print(*res_list[1:])