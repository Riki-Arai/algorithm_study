H, W = map(int, input().split())

grid_list = []
for _ in range(H):
    a = input()
    if a != "." * W:
        grid_list.append(a)

new_grid_list = grid_list.copy()
new_h = len(grid_list)
if new_h == 1:
    res_grid_list = [grid for grid in new_grid_list[0] if grid != "."]
    print("".join(res_grid_list))
    exit()

del_count = 0
for j in range(W):
    tmp = ""
    for i in range(new_h):
        tmp += grid_list[i][j]
        if tmp == "." * new_h:
            new_grid_list = [grid[:j-del_count] + grid[j-del_count+1:] for grid in new_grid_list]
            del_count += 1

for grid in new_grid_list:
    print(grid)
