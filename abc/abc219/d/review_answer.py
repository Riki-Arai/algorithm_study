N = int(input())
X, Y = map(int, input().split())

dp_lists = [[float("INF")]*(300+1) for _ in range(300+1)]
dp_lists[0][0] = 0
for _ in range(N):
    A, B = map(int, input().split())
    for i in range(300, -1, -1):
        for j in range(300, -1, -1):
            if dp_lists[i][j] == float("INF"):
                continue
            ni = min(300, i+A)
            nj = min(300, j+B)
            dp_lists[ni][nj] = min(dp_lists[i][j]+1, dp_lists[ni][nj])

res = float("INF")
for i in range(301):
    for j in range(301):
        if i >= X and j >= Y:
            res = min(dp_lists[i][j], res)

if res == float("INF"):
    print(-1)
else:
    print(res)