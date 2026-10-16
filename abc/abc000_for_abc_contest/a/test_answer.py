import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
N, M = map(int, input().split()) # 取得例：1 2
S = input().strip() # 取得例："A"
S, T = input().split() # 取得例："A" "B"
S_list = list(input()) # 取得例：["A","B"・・・]
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
A_list = input().split() # 取得例：["A","B","C"]、1行の入力用
A_list = [input() for _ in range(N)] # 取得例：["A","B"・・・"E"]、N行の入力用
A_list = [int(input()) for _ in range(N)] # 取得例：[A1,A2・・・An]、N行の入力用(int型に変換)
g_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解
input_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]、空白区切りの数値入力
input_lists = [list(map(int, list(input()))) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]、12や34のようの連続文字列をint型に変換してリスト化
input_lists = [input().split() for _ in range(N)] # 取得例:[["A","B"], ["B",2]・・["F",6]]、2列の入力を型変換せずに取得
input_lists = [[s, int(x)] for s, x in (input().split() for _ in range(N))] # 取得例:[["A",1], ["B",2]・・["E",5]]
input_lists = [[int(x), s] for x, s in (input().split() for _ in range(N))] # 取得例:[[1,"A"], [2,"B"] ・・[5,"E"]]

import sys

A_lists = []
for i in sys.stdin:
    A_lists.append(i.strip())



INF = 10**36
def bellman_ford_all_negative(G, s):
    """
    1つのスタート地点を起点とした最短経路を求める時に使用し、計算量はO(VE)(すべての点を対象にする場合はワーシャルフロイド法)
    s: スタートとなる頂点の番号
    G: 隣接グラフ(例：[[(1, 10), (3, 50)], [(2, 20)], [(3, -40)], [(1, 10)]])
    
    返り値:
    costs: 頂点sからの最小コスト（負の閉路がある場合は正確なものではなくなるので注意）
    negative: ある頂点が負の閉路の影響を受けるかどうかの真偽値リスト
    """
    n = len(G)
    costs = [INF] * n
    costs[s] = 0
    
    # 1. 通常の最短経路計算（V-1回の更新）
    for _ in range(n - 1):
        for v in range(n):
            if costs[v] == INF:
                continue
            for to, c in G[v]:
                if costs[to] > costs[v] + c:
                    costs[to] = costs[v] + c
                    
    # 2. 負の閉路の検出と影響の伝播（さらにV回の更新）
    # negative[i] = True なら、スタートから頂点iへのコストは -無限大
    negative = [False] * n
    
    for _ in range(n):
        for v in range(n):
            if costs[v] == INF:
                continue
            for to, c in G[v]:
                # 「通常通り更新される」または「遷移元がすでに負の閉路の影響下にある」場合
                if costs[to] > costs[v] + c or negative[v]:
                    costs[to] = costs[v] + c
                    negative[to] = True
                    
    return costs, negative