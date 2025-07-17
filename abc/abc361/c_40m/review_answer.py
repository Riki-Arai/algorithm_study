N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

A_list.sort()
res = float("INF")
for i in range(K+1):
    res = min(A_list[-(K-i)-1] - A_list[i], res)

print(res)