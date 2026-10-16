'''
(1) 最初は片方を固定する方針で検討したがうまくはまらず
(2) 状況によっては片方があえて前進と後退を繰り返した方が良い場合もあってややこしい
(3) よって両者を動かしてパターンを全探索する形を考えてみたところ、計算量的に間に合うことがわかった
(4) そこでBFSを用いて実装をしたが、ただし二つのコマの動きを同時にキューに入れる工夫などをした
'''
from collections import deque

T = int(input()) # 数値：1

for _ in range(T):
    N, M = map(int, input().split()) # 取得例：1 2
    C_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
    g_lists = [[[], []] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split()) # 取得例：1 2
        g_lists[u][C_list[v-1]].append(v)
        g_lists[v][C_list[u-1]].append(u)

    if C_list[0] == C_list[-1]:
        print(-1)
        continue

    res = float("INF")
    dq = deque([(1, N, 0)])
    seen_sets = set([(1, N)])
    while len(dq):
        t, a, dis = dq.popleft()
        for n_t in g_lists[t][0]:
            for n_a in g_lists[a][1]:
               n_place = (n_t, n_a)
               if n_t == N and n_a == 1:
                   res = min(dis+1, res)
                   continue
               if n_place not in seen_sets:
                   seen_sets.add(n_place)
                   dq.append((n_t, n_a, dis+1))

        for n_t in g_lists[t][1]:
            for n_a in g_lists[a][0]:
               n_place = (n_t, n_a)
               if n_t == N and n_a == 1:
                   res = min(dis+1, res)
                   continue
               if n_place not in seen_sets:
                   seen_sets.add(n_place)
                   dq.append((n_t, n_a, dis+1))

    if res == float("INF"):
        print(-1)
    else:
        print(res)