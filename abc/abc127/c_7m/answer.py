N, M = map(int, input().split()) # 取得例：1 2
A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

max_l = 0
min_r = float("INF")
for l, r in A_lists:
    max_l = max(l, max_l)
    min_r = min(r, min_r)

res = 0
for i in range(1, N+1):
    if max_l <= i <= min_r:
        res += 1

print(res)