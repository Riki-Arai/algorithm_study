N = int(input()) # 取得例：1
X_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = float("INF")
for i in range(1, 101):
    tmp_res = 0
    for x in X_list:
        tmp_res += pow(x-i, 2)
    res = min(tmp_res, res)

print(res)