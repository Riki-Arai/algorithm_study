H, W, X, Y = map(int, input().split())
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

res = 1
# 上、右、下、左
move_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for m in move_list:
    xx, yy = X - 1, Y - 1
    while True:
        if xx + m[0] >= 0 and xx + m[0] < H and yy + m[1] >= 0 and yy + m[1] < W:
            xx += m[0]
            yy += m[1]
            if S_lists[xx][yy] == ".":
                res += 1
            else:
                break
        else:
            break

print(res)