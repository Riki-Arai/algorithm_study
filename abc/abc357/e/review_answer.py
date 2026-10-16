'''
※実装はGPT
(1) 閉路にまつわる問題である可能性だと考え、そこから閉路に含まれるものとそうではないものという切り分けはできた
(2) しかし実装ができずにWAとなってしまった
(3) 実装が必要以上に複雑になったように感じる
'''
from collections import deque
from atcoder.dsu import DSU

N = int(input())
A_list = list(map(int, input().split()))

g_lists = [[] for _ in range(N + 1)]
rev_g_lists = [[] for _ in range(N + 1)]
dsu = DSU(N + 1)

for i, a in enumerate(A_list, 1):
    g_lists[i].append(a)
    rev_g_lists[a].append(i)
    dsu.merge(i, a)

res = 0

for g_list in dsu.groups()[1:]:
    # cycle を見つける
    dq = deque()
    seen_set = set()

    a = g_list[0]
    while a not in seen_set:
        seen_set.add(a)
        dq.append(a)
        a = g_lists[a][0]

    # cycle の頂点を取り出す
    cir_set = set()

    while True:
        b = dq.pop()
        cir_set.add(b)
        if b == a:
            break

    # cycle 同士の到達
    res += len(cir_set) ** 2

    ################### ここから以下がうまく実装できず
    # cycle に流れ込む頂点を DFS/BFS
    for c in cir_set:
        q = deque()

        for b in rev_g_lists[c]:
            if b in cir_set:
                continue
            q.append((b, 1))

        while q:
            b, dist = q.popleft()

            # b からは
            # 自身を含めて dist 個の木部分
            # + cycle 全体
            res += dist + len(cir_set)

            for x in rev_g_lists[b]:
                if x in cir_set:
                    continue
                q.append((x, dist + 1))

print(res)