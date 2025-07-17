N = int(input()) # 数値
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = float("INF")
for A_list in A_lists:
    a, p, x = A_list
    if x - (((a+0.5) // 1)) > 0:
        res = min(res, p)

if res == float("INF"):
    print(-1)
else:
    print(res)