import sys; sys.setrecursionlimit(10**7)

H, W = map(int, input().split()) # 取得例：1 2
g_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

