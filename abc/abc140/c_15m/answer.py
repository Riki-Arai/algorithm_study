N = int(input()) # 数値：1
B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res_list = [float("INF")] * N
for i in range(len(B_list)):
    v = B_list[i]
    res_list[i] = min(res_list[i], v)
    res_list[i+1] = min(res_list[i+1], v)

print(sum(res_list))