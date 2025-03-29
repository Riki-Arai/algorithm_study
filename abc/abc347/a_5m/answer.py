N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = []
for a in A_list:
    if a % K == 0:
        res_list.append(int(a / K))

print(*res_list)