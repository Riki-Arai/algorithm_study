H, W, N = map(int, input().split())

grid_list = [["."]*W for _ in range(H)]
move_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
m_idx, x_idx, y_idx = 0, 0, 0
for _ in range(N):
    if grid_list[x_idx][y_idx] == '.':
        grid_list[x_idx][y_idx] = '#'
        m_idx = (m_idx + 1) % 4
        x_idx += move_list[m_idx][0] 
        y_idx += move_list[m_idx][1] 
    else:
        grid_list[x_idx][y_idx] = '.' 
        m_idx = (m_idx - 1) % 4
        x_idx += move_list[m_idx][0] 
        y_idx += move_list[m_idx][1] 

    x_idx = (x_idx + H) % H
    y_idx = (y_idx + W) % W

for grid in grid_list:
    print("".join(grid))