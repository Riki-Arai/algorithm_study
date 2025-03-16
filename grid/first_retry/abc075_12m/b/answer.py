N, M = map(int, input().split())
S_list = [list(input()) for _ in range(N)]

# 上、右上、右、右下、下、左下、左、左上
move_list = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
for i in range(N):
    res = ""
    for j in range(M):
        if S_list[i][j] == ".":
            b_count = 0
            for m in move_list:
                h, w = i, j
                h += m[0]
                w += m[1]
                if h < N and h >= 0 and w < M and w >= 0 and S_list[h][w] == "#":
                    b_count += 1

            res += str(b_count)
        else:
            res += "#"

    print(res)