'''
(1) 一見すると削除を考えるとO(QN)にも感じるが、実際には双方の点において1つずつしか追加されない
(2) よって仮に10**5回分の追加があっても、削除自体は1回だけ2*10**5をやれば済んでしまうのでO(QN)にはならない
(3) あとはsetを用いて素朴に実装をすればいい
(4) 基本的に1つ追加→削除のようなケースは実は計算量で間に合うケースが多いことを意識しておくと良さそう
'''
import sys; sys.setrecursionlimit(10**7)

N, Q = map(int, input().split()) # 取得例：1 2

res = N
g_lists = [set() for _ in range(N+1)]
for _ in range(Q):
    input_ = input()
    if input_[0] == "1":
        _, u, v = map(int, input_.split())
        if not len(g_lists[u]):
            res -= 1
        if not len(g_lists[v]):
            res -= 1
        g_lists[u].add(v)
        g_lists[v].add(u)
    else:
        _, v = map(int, input_.split())
        if len(g_lists[v]):
            for u in g_lists[v]:
                if len(g_lists[u]) == 1:
                    res += 1
                g_lists[u].discard(v)

            res += 1
            g_lists[v] = set()

    print(res)