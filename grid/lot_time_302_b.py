H, W = map(int, input().split())
s_list = [input() for _ in range(H)]
move_list = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]

for i in range(H):
    for j in range(W):
        if s_list[i][j] == "s":
            for h, w in move_list:
                res_list = [[i+1, j+1]]
                i_m = i
                j_m = j
                want_str = "s"
                count = 0
                while count < 5:
                    i_m += h
                    j_m += w
                    count += 1
                    if i_m >= 0 and i_m < H and j_m >= 0 and j_m < W:
                        want_str += s_list[i_m][j_m]
                        res_list.append([i_m+1, j_m+1])

                if want_str == "snuke":
                    for res in res_list:
                        print(res[0], res[1])
                    exit()
