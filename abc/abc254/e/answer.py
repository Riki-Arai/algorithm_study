'''
(1) 次数と距離が双方とも3以下、かつ処理時間も3.5秒以内というのがヒント
(2) 3より上の距離を探索する意味がないことを考えると1つの頂点を起点としたときに探索数は最大でも30個程度
(3) よってN*30で見積もっても間に合うことがわかるので、あとは3以内の頂点の番号の合計をBFSで計算をすればいい
'''
from collections import deque

N, M = map(int, input().split()) # 取得例：1 2
g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split()) # 取得例：1 2
    g_lists[a].append(b)
    g_lists[b].append(a)

Q = int(input()) # 数値：1
for _ in range(Q):
    x, k = map(int, input().split()) # 取得例：1 2

    res = 0
    dq = deque([(x, 0)])
    seen_set = set([x])
    while len(dq):
        u, dis = dq.popleft()
        if dis > k:
            continue

        res += u
        for v in g_lists[u]:
            if v not in seen_set :
                seen_set.add(v)
                dq.append((v, dis+1))

    print(res)