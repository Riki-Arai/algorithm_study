N = int(input())

ans = [[None] * N for _ in range(N)]
c = N // 2
ans[c][c] = "T"

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右, 下, 左, 上
d = 0
i, j = 0, 0
for x in range(1, N * N):
    ans[i][j] = x

    ni = i + dirs[d][0]
    nj = j + dirs[d][1]

    if not (0 <= ni < N and 0 <= nj < N) or ans[ni][nj] is not None:
        d = (d + 1) % 4
        ni = i + dirs[d][0]
        nj = j + dirs[d][1]

    i, j = ni, nj

for row in ans:
    print(*row)