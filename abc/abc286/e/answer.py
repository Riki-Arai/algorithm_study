'''
(1) はじめからワーシャルフロイド法を考えてはいたが、慣れていないこともあってダイクストラ法で解いてしまったがやはりTLE
(2) 計算量的には使えそうだが、工夫が必要なので復習後に問題を解き直す
(3) 距離はわかりやすい一方で、重みが頂点に存在するため戸惑ったが、中間地点となる重み分は-にして対応
(4) WAとなった原因で、最小距離を更新する場合は重みが小さくても更新する必要がある
    →二変数の最適化をする際には今回の処理は使える場面はありそう
'''
N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
S_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

g_lists = [[(float("INF"), -float("INF"))]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if S_lists[i][j] == "Y":
            g_lists[i][j] = (1, A_list[i]+A_list[j])

for k in range(N):
    for s in range(N):
        for t in range(N):
            if g_lists[s][t][0] > g_lists[s][k][0] + g_lists[k][t][0]:
                g_lists[s][t] = (g_lists[s][k][0]+g_lists[k][t][0], g_lists[s][k][1]+g_lists[k][t][1]-A_list[k])
            elif g_lists[s][t][0] == g_lists[s][k][0] + g_lists[k][t][0]:
                g_lists[s][t] = (g_lists[s][t][0], max(g_lists[s][t][1], g_lists[s][k][1]+g_lists[k][t][1]-A_list[k]))

Q = int(input()) # 数値：1
for _ in range(Q):
    U, V = map(int, input().split()) # 取得例：1 2
    U -= 1
    V -= 1
    if g_lists[U][V][0] != float("INF") and g_lists[U][V][1] != -float("INF"):
        print(g_lists[U][V][0], g_lists[U][V][1])
    else:
        print("Impossible")