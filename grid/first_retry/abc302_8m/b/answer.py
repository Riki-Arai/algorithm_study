H, W = map(int, input().split())
A_list = [input() for _ in range(H)]

# 上、右上、右、右下、下、左下、左、左上
move_list = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
for i in range(H):
    for j in range(W):
        for m in move_list:
            res = ""
            res_list = []
            ii, jj = i, j
            res += A_list[ii][jj]
            res_list.append((ii, jj))
            for _ in range(4):
                ii = ii + m[0]
                jj = jj + m[1]
                if ii >= 0 and jj >= 0 and ii < H and jj < W:
                    res += A_list[ii][jj]
                    res_list.append((ii, jj))

            if res == "snuke":
                for res in res_list:
                    print(res[0]+1, res[1]+1)
                exit()