import sys; sys.setrecursionlimit(10**7)

H, W = map(int, input().split()) # 取得例：1 2

grid_lists = [["."]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i == 0 or i == H-1:
            grid_lists[i][j] = "#"
        if j == 0 or j == W-1:
            grid_lists[i][j] = "#"

for grid_list in grid_lists:
    print("".join(grid_list))