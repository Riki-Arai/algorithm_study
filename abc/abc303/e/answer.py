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
# はじめの葉をキューに追加
for i, e in enumerate(e_list[1:], 1):
    if e == 1:
        dq.append(i)

res_list = []
while dq:
    u = dq.popleft()
    # 既に削除された頂点ならスキップ
    if u in seen_set:
        continue
    
    # 距離1の頂点（星の中心）を見つける
    root = -1
    for v in g_lists[u]:
        if v not in seen_set:
            root = v
            break
            
    if root == -1:
        continue
        
    # 選んだ葉から距離2以下の頂点を集める
    # (u: 距離0, root: 距離1, v: 距離2)
    removed_nodes = [u, root]
    for v in g_lists[root]:
        if v != u and v not in seen_set:
            removed_nodes.append(v)
            
    # 頂点の個数が x 個のとき、レベル x-1 の星
    x = len(removed_nodes)
    res_list.append(x - 1)
    
    # 数えた頂点および隣接する辺を T から削除する
    for v in removed_nodes:
        seen_set.add(v)
        # 削除された頂点に隣接している外側の頂点の次数（辺）を減らす
        for vv in g_lists[v]:
            if vv not in seen_set:
                e_list[vv] -= 1
                # 次数が1になったら新たな葉としてキューに追加
                if e_list[vv] == 1:
                    dq.append(vv)

print(*sorted(res_list))