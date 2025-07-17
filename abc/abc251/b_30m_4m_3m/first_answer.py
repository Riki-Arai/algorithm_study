N, W = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = []
for i in range(N):
    if A_list[i] <= W:
        res_list.append(A_list[i])
    for j in range(i+1, N):
        if A_list[i] + A_list[j] <= W:
            res_list.append(A_list[i] + A_list[j])
        for k in range(j+1, N):
            if A_list[i] + A_list[j] + A_list[k] <= W:
                res_list.append(A_list[i] + A_list[j] + A_list[k])

print(len(set(res_list)))