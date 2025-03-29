N, L, R = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = []
for a in A_list:
    x_dis = abs(L-a)
    l_flag, r_flag = False, False
    if x_dis <= abs(L-a) and x_dis <= abs(R-a):
        l_flag = True
    x_dis = abs(R-a)
    if x_dis <= abs(L-a) and x_dis <= abs(R-a):
        r_flag = True

    if l_flag and r_flag:
        res_list.append(L)
    elif r_flag:
        res_list.append(R)
    elif l_flag:
        res_list.append(L)

print(*res_list)