H, W  = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(H)] # 取得例:[[1,2], [3,4]・・[9,10]]

min_v = float("INF")
for i in range(H):
    for j in range(W):
        min_v = min(min_v, A_lists[i][j])

res = 0
for i in range(H):
    for j in range(W):
        res += A_lists[i][j] - min_v

print(res)