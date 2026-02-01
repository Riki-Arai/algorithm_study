N = int(input()) # 数値
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
for l in range(N):
    tmp_res = 0
    min_v = float("INF")
    for i in range(l, N):
        min_v = min(A_list[i], min_v)
        tmp_res = max(min_v*(i-l+1), tmp_res)

    res = max(tmp_res, res)

print(res)