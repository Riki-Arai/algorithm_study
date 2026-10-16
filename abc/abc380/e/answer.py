import sys
from collections import defaultdict
from atcoder.dsu import DSU

sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())

dsu = DSU(N + 1)

# DSUの代表 -> 色
g2c_dict = defaultdict(int)

# 色 -> その色のマス数
c2s_dict = defaultdict(int)

# DSUの代表 -> 区間の左端
g2l_dict = defaultdict(int)

# DSUの代表 -> 区間の右端
g2r_dict = defaultdict(int)

for n in range(1, N + 1):
    g2c_dict[dsu.leader(n)] = n
    c2s_dict[n] = 1
    g2l_dict[dsu.leader(n)] = n
    g2r_dict[dsu.leader(n)] = n

for _ in range(Q):
    input_ = input().strip()

    if input_[0] == "1":
        _, x, c = map(int, input_.split())

        # xが属する現在の連結成分
        g1 = dsu.leader(x)
        g1_size = dsu.size(x)

        # すでに目的の色なら何もしない
        if g2c_dict[g1] == c:
            continue

        # 現在の色の個数を減らす
        c2s_dict[g2c_dict[g1]] -= g1_size

        # 新しい色の個数を増やす
        c2s_dict[c] += g1_size

        # 区間全体を c に塗り替える
        g2c_dict[g1] = c

        # -------------------------
        # 左隣の区間とマージ
        # -------------------------
        if g2l_dict[g1] > 1:
            g2 = dsu.leader(g2l_dict[g1] - 1)

            if g1 != g2 and g2c_dict[g2] == c:
                # マージ前の区間情報を保存
                g1_l = g2l_dict[g1]
                g1_r = g2r_dict[g1]
                g2_l = g2l_dict[g2]
                g2_r = g2r_dict[g2]

                # 古い代表の情報を削除
                del g2c_dict[g1]
                del g2c_dict[g2]

                del g2l_dict[g1]
                del g2l_dict[g2]

                del g2r_dict[g1]
                del g2r_dict[g2]

                # DSUでマージ
                g1 = dsu.merge(g1, g2)

                # 新しい代表に情報を登録
                g2c_dict[g1] = c
                g2l_dict[g1] = min(g1_l, g2_l)
                g2r_dict[g1] = max(g1_r, g2_r)

        # -------------------------
        # 右隣の区間とマージ
        # -------------------------
        g1 = dsu.leader(x)

        if g2r_dict[g1] < N:
            g2 = dsu.leader(g2r_dict[g1] + 1)

            if g1 != g2 and g2c_dict[g2] == c:
                # マージ前の区間情報を保存
                g1_l = g2l_dict[g1]
                g1_r = g2r_dict[g1]
                g2_l = g2l_dict[g2]
                g2_r = g2r_dict[g2]

                # 古い代表の情報を削除
                del g2c_dict[g1]
                del g2c_dict[g2]

                del g2l_dict[g1]
                del g2l_dict[g2]

                del g2r_dict[g1]
                del g2r_dict[g2]

                # DSUでマージ
                g1 = dsu.merge(g1, g2)

                # 新しい代表に情報を登録
                g2c_dict[g1] = c
                g2l_dict[g1] = min(g1_l, g2_l)
                g2r_dict[g1] = max(g1_r, g2_r)

    else:
        c = int(input_.split()[1])
        print(c2s_dict[c])