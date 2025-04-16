N, L, R = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = []
for a in A_list:
    if a <= L:
        res_list.append(L)
    elif a >= R:
        res_list.append(R)
    else:
        res_list.append(a)

print(*res_list)