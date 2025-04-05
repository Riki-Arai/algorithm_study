N, C = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = [A_list.pop(0)]
for a in A_list:
    if a - res_list[-1] >= C:
        res_list.append(a)
print(len(res_list))