import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
from collections import defaultdict


def draw_weighted_graph(G):
    # ==================================================
    # 連結成分を取得
    # ==================================================
    components = sorted(
        nx.connected_components(G),
        key=len,
        reverse=True
    )

    pos = {}

    # ==================================================
    # 最大の連結成分をメインとして配置
    # ==================================================
    main_nodes = list(components[0])
    main_graph = G.subgraph(main_nodes)

    # MultiGraph のままだとレイアウトが不安定になるので、
    # レイアウト計算だけ通常のGraphを使用
    layout_graph = nx.Graph(main_graph)

    main_pos = nx.spring_layout(
        layout_graph,
        seed=42,
        k=2.2,          # ノード間の距離
        iterations=500,
        scale=4.0
    )

    for node, p in main_pos.items():
        pos[node] = p

    # ==================================================
    # メイン以外の連結成分を右側に配置
    # ==================================================
    other_components = components[1:]

    for i, component in enumerate(other_components):
        nodes = list(component)

        # 右側の配置位置
        x = 6.0
        y = 3.5 - i * 2.5

        if len(nodes) == 1:
            # 孤立した頂点
            pos[nodes[0]] = (x, y)

        else:
            # 複数頂点からなる連結成分
            subgraph = G.subgraph(nodes)

            sub_pos = nx.circular_layout(
                nx.Graph(subgraph),
                scale=1.0
            )

            for node, p in sub_pos.items():
                pos[node] = (
                    x + p[0],
                    y + p[1]
                )

    # ==================================================
    # 図の大きさ
    # ==================================================
    fig, ax = plt.subplots(
        figsize=(16, 12)
    )

    # ==================================================
    # ノード描画
    # ==================================================
    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=1300,
        node_color="lightblue",
        edgecolors="black",
        linewidths=2,
        ax=ax
    )

    # ==================================================
    # ノード番号
    # ==================================================
    nx.draw_networkx_labels(
        G,
        pos,
        font_size=14,
        font_weight="bold",
        ax=ax
    )

    # ==================================================
    # 同じ頂点間の辺をグループ化
    #
    # 例：
    # 7 -- 10 が2本ある
    # 8 -- 10 が2本ある
    # ==================================================
    edge_groups = defaultdict(list)

    for u, v, key, data in G.edges(
        keys=True,
        data=True
    ):
        pair = tuple(sorted((u, v)))

        edge_groups[pair].append(
            (
                u,
                v,
                key,
                data["weight"]
            )
        )

    # ==================================================
    # 辺と重みを描画
    # ==================================================
    for pair, edges in edge_groups.items():

        count = len(edges)

        # ----------------------------------------------
        # 重複辺の曲がり具合
        # ----------------------------------------------
        if count == 1:
            radians = [0.0]

        elif count == 2:
            radians = [-0.28, 0.28]

        elif count == 3:
            radians = [-0.35, 0.0, 0.35]

        else:
            center = (count - 1) / 2
            radians = [
                (i - center) * 0.25
                for i in range(count)
            ]

        # ----------------------------------------------
        # 各辺を描画
        # ----------------------------------------------
        for edge, rad in zip(edges, radians):

            u, v, key, weight = edge

            nx.draw_networkx_edges(
                G,
                pos,
                edgelist=[(u, v, key)],
                width=2.3,
                edge_color="gray",
                alpha=0.9,
                connectionstyle=f"arc3,rad={rad}",
                ax=ax
            )

            # ------------------------------------------
            # 重み表示位置
            # ------------------------------------------
            x1, y1 = pos[u]
            x2, y2 = pos[v]

            # 辺の中央
            x = (x1 + x2) / 2
            y = (y1 + y2) / 2

            # 辺に対して垂直な方向へずらす
            dx = x2 - x1
            dy = y2 - y1

            length = math.sqrt(
                dx * dx + dy * dy
            )

            if length != 0:
                perp_x = -dy / length
                perp_y = dx / length

                # 曲線の大きさに合わせて移動
                offset = rad * 1.0

                x += perp_x * offset
                y += perp_y * offset

            # ------------------------------------------
            # 重みを表示
            # 白背景をつけて読みやすくする
            # ------------------------------------------
            ax.text(
                x,
                y,
                str(weight),
                fontsize=11,
                fontweight="bold",
                ha="center",
                va="center",
                zorder=5,
                bbox=dict(
                    boxstyle="round,pad=0.2",
                    facecolor="white",
                    edgecolor="gray",
                    alpha=0.95
                )
            )

    # ==================================================
    # 軸を非表示
    # ==================================================
    ax.axis("off")

    # 縦横比を固定
    ax.set_aspect("equal")

    # 余白
    ax.margins(0.15)

    # レイアウト調整
    plt.tight_layout()

    # ==================================================
    # PNG保存
    # ==================================================
    plt.savefig(
        "graph.png",
        dpi=200,
        bbox_inches="tight"
    )

    # ==================================================
    # 画面表示
    # ==================================================
    plt.show()


def main():

    # --------------------------------------------------
    # N = 頂点数
    # M = 辺数
    # --------------------------------------------------
    N, M = map(int, input().split())

    # 多重辺を許す無向グラフ
    G = nx.MultiGraph()

    # 頂点を追加
    G.add_nodes_from(range(1, N + 1))

    # --------------------------------------------------
    # 入力
    #
    # u v w
    # u-v が重み w の辺
    # --------------------------------------------------
    for _ in range(M):
        u, v, w = map(int, input().split())

        G.add_edge(
            u,
            v,
            weight=w
        )

    # グラフ描画
    draw_weighted_graph(G)


if __name__ == "__main__":
    main()
