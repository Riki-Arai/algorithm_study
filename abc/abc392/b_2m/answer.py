N, M = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = []
for i in range(1, N+1):
    if i not in A_list:
        res_list.append(i)
print(N-M)
print(*res_list)