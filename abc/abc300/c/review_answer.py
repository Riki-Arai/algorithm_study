H, W = map(int, input().split())
C_lists = [list(input()) for _ in range(H)]

res_list = [0] * min(H, W)
center_lists = []
for i in range(H):
    for j in range(W):
        if C_lists[i][j] == "#":
            cross_flag = True
            for k in [1, -1]:
                for l in [1, -1]:
                    if not(0 <= i+k < H and 0 <= j+l < W and C_lists[i+k][j+l] == "#"):
                        cross_flag = False
            if cross_flag:
                center_lists.append([i, j])

for i, j in center_lists:
    n = 1
    while True:
        cross_flag = True
        for k in [n, -n]:
            for l in [n, -n]:
                if not(0 <= i+k < H and 0 <= j+l < W and C_lists[i+k][j+l] == "#"):
                    cross_flag = False
        if not cross_flag:
            res_list[n-2] += 1
            break
        n += 1

print(*res_list)