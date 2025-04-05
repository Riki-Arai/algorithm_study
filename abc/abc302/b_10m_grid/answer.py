H, W = map(int, input().split())
A_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

# 上、右上、右、右下、下、左下、左、左上
move_list = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
for i in range(H):
    for j in range(W):
        for m in move_list:
            h, w = i, j
            target = A_lists[i][j]
            res_list = [(i+1, j+1)]
            hh, ww = m[0], m[1]
            for _ in range(4):
                h = h + hh
                w = w + ww
                if h >= 0 and h < H and w >= 0 and w < W:
                    target += A_lists[h][w]
                    res_list.append((h+1, w+1))
                else:
                    break
            if target == "snuke":
                for res in res_list:
                    print(res[0], res[1])
                