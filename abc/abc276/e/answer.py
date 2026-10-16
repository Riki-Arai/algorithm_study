'''
(1) バックトラックが必要かと思っていたが、Sに戻れる時点で4以上の距離になる性質を踏まえるとその処理は不要
(2) C++だと余裕で間に合った（言語でTLEの有無が変わるのはどうかと思うが・・・）
'''
import sys; sys.setrecursionlimit(10**7)

H, W = map(int, input().split()) # 取得例：1 2
g_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

for i in range(H):
    for j in range(W):
        if g_lists[i][j] == "S":
            s_i, s_j = i, j
            break

seen_sets = set()
move_lists = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}.values()
def dfs(i, j, dis):
    seen_sets.add((i, j))
    for mi, mj in move_lists:
        ii = i + mi
        jj = j + mj
        if 0 <= ii < H and 0 <= jj < W and g_lists[ii][jj] == "S" and dis+1 >= 4:
            print("Yes")
            exit()

        if 0 <= ii < H and 0 <= jj < W and g_lists[ii][jj] == "." and (ii, jj) not in seen_sets:
            seen_sets.add((ii, jj))
            dfs(ii, jj, dis+1)

dfs(s_i, s_j, 0)
print("No")