# 緑diff手前なので身構えてDFSを検討してしまったが、B問題のような解き方でいけた
# 計算量の見積もりが48*N*Nだと気づけば十分間に合うとわかることが重要そう
N = int(input())
S_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

# 上、右上、右、右下、下、左下、左、左上
move_lists = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
for i in range(N):
    for j in range(N):
        if S_lists[i][j] == "#":
            for mj, mi in move_lists:
                ii, jj = i, j
                w_num = 0
                count = 1
                for _ in range(5):
                    ii += mi
                    jj += mj
                    #　gridの枠からはみ出たらそもそも終了
                    if not (0 <= ii < N and 0 <= jj < N):
                        break
                    elif S_lists[ii][jj] == ".":
                        w_num += 1
                        # 白色で2回以上塗ってしまっているならbreak
                        if w_num > 2:
                            break
                        count += 1
                    # 残りの条件は黒色を通過しているので+1
                    else:
                        count += 1

                    if count == 6:
                        print("Yes")
                        exit()

print("No")