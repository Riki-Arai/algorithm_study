N, M = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = []
res_lists = []
n_list = [i for i in range(1, N+1)]
for n in n_list:
    if n in A_list:
        res_list.append(n)
    else:
        res_list.append(n)
        res_lists.append(res_list[::-1])
        res_list = []

print(*sum(res_lists, []))