N = int(input())

grid_lists = [[None]*N for _ in range(N)]
move_lists = [(0, 1), (1, 0), (0, -1), (-1, 0)]
i, j = 0, 0
grid_lists[i][j] = 1
m_i = 0
count = 2
while True:
    mi, mj = move_lists[m_i]
    ii = i + mi
    jj = j + mj
    if count == N*N:
        grid_lists[ii+1][jj+1] = "T"
        break

    if 0 <= ii < N and 0 <= jj < N and grid_lists[ii][jj] is None:
        grid_lists[ii][jj] = str(count)
        count += 1
    else:
        m_i = (m_i+1)%4
        mi, mj = move_lists[m_i]
        ii = i + mi
        jj = j + mj
        grid_lists[ii][jj] = str(count)
        count += 1
    i = ii
    j = jj

for grid_list in grid_lists:
    print(*grid_list)