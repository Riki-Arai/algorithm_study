'''
(1) 1つの枝の数しか持たない葉に着目し、その葉の根を見つける
(2) その根の持つ葉のうちでまだ探索しておらず、かつ枝が2つあれば接続部分の可能性が高い
(3) 接続先の頂点をキューに格納し、(1)と(2)を繰り返すイメージ
(4) しかしこの実装は正直複雑で、解説を読んでみると距離に着目していた
(5) 今回の問題では距離は全く考えていなかったので、グラフに問題では頂点や辺の数だけではなく距距にも注目をするべきだった
'''
from collections import deque

N = int(input()) # 数値：1

g_lists = [[] for _ in range(N+1)]
e_list = [0]*(N+1)
for _ in range(N-1):
    u, v = map(int, input().split()) # 取得例：1 2
    g_lists[u].append(v)
    g_lists[v].append(u)
    e_list[u] += 1
    e_list[v] += 1

seen_set = set()
dq = deque()
for i, e in enumerate(e_list[1:], 1):
    if e == 1:
        dq.append(i)
        seen_set.add(i)

res_list = []
while len(dq):
    u = dq.popleft()
    root = g_lists[u][0]
    if root in seen_set:
        continue
    seen_set.add(root)
    res_list.append(e_list[root])
    for v in g_lists[root]:
        if e_list[v] == 2 and v not in seen_set:
            for vv in g_lists[v]:
                if vv != root and vv not in seen_set:
                    dq.append(vv)
                    g_lists[vv].remove(v)
                    e_list[vv] -= 1
                seen_set.add(vv)
        seen_set.add(v)

print(*sorted(res_list))