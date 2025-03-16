H, W, N = map(int, input().split())

grid_list = [["."]*W for _ in range(H)]
move_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
m_idx, x_idx, y_idx = 0, 0, 0
count = 0
while count < N:
    if grid_list[x_idx][y_idx] == '.':
        grid_list[x_idx][y_idx] = '#'
        m_idx += 1
        if m_idx == 4:
            m_idx = 0
        x_idx += move_list[m_idx][0] 
        y_idx += move_list[m_idx][1] 
    else:
        grid_list[x_idx][y_idx] = '.' 
        m_idx -= 1
        if m_idx < 0:
            m_idx = 3
        x_idx += move_list[m_idx][0] 
        y_idx += move_list[m_idx][1] 

    if x_idx < 0:
        x_idx = H - 1
    elif x_idx == H:
        x_idx = 0

    if y_idx < 0:
        y_idx = W - 1
    elif y_idx == W:
        y_idx = 0
        
    count += 1

for grid in grid_list:
    print("".join(grid))