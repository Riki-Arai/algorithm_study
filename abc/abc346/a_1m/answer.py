N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = []
for i in range(1, N):
    res_list.append(A_list[i-1] * A_list[i])

print(*res_list)