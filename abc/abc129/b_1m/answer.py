N = int(input()) # 数値：1
W_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = float("INF")
for i in range(1, N):
    res = min(abs(sum(W_list[:i]) - sum(W_list[i:])), res)

print(res)