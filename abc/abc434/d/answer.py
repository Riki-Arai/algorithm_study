N = int(input().strip())

# H: 行数, W: 列数
H, W = 2000, 2000
imos_lists = [[[0, 0] for _ in range(W+2)] for _ in range(H + 2)]
for i in range(1, N+1):
    y1, y2, x1, x2 = map(int, input().split())
    imos_lists[y1][x1][0] += 1          # 左上（始点）
    imos_lists[y1][x1][1] += i

    imos_lists[y1][x2+1][0] -= 1      # 右上（x方向の終点の 1つ右）
    imos_lists[y1][x2+1][1] -= i     # 右上（x方向の終点の 1つ右）

    imos_lists[y2 + 1][x1][0] -= 1      # 左下（y方向の終点の 1つ下）
    imos_lists[y2 + 1][x1][1] -= i      # 左下（y方向の終点の 1つ下）

    imos_lists[y2 + 1][x2 + 1][0] += 1  # 右下（重複して引いた分を戻す）
    imos_lists[y2 + 1][x2 + 1][1] += i  # 右下（重複して引いた分を戻す）

# 横方向の累積和
for y in range(1, H + 2):
    for x in range(1, W + 2):
        imos_lists[y][x][0] += imos_lists[y][x - 1][0]
        imos_lists[y][x][1] += imos_lists[y][x - 1][1]

# 縦方向の累積和
for y in range(1, H + 2):
    for x in range(1, W + 2):
        imos_lists[y][x][0] += imos_lists[y - 1][x][0]
        imos_lists[y][x][1] += imos_lists[y - 1][x][1]

cov_n = 0
single_list = [0]*(N+1)
for i in range(H+2):
    for j in range(W+2):
        if imos_lists[i][j][0] > 0:
            cov_n += 1
        if imos_lists[i][j][0] == 1:
            single_list[imos_lists[i][j][1]] += 1

total = 2000*2000
for n in range(1, N+1):
    print(total-(cov_n-single_list[n]))