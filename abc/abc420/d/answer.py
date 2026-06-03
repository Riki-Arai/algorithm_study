from collections import deque

H, W = map(int, input().split()) # 取得例：1 2
A_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

for i in range(H):
    for j in range(W):
        if A_lists[i][j] == "S":
            s_x, s_y = i, j
        elif A_lists[i][j] == "G":
            g_x, g_y = i, j