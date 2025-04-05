N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = []
for i, a in enumerate(A_list):
    if i == 0:
        res_list.append(a)
    else:
        res_list.append(a - A_list[i-1])

print(*res_list)