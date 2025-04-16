N, Q = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(Q)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
res_list = [1] * N
pos_dic = {i+1: i for i in range(N)}
for A_list in A_lists:
    if A_list[0] == 2:
        print(res)
    else:
        b_pos = pos_dic[A_list[1]]
        n_pos = A_list[2] - 1
        if res_list[b_pos] == 2:
            if res - 1 >= 0:
                res -= 1
            else:
                res = 0

        if res_list[n_pos] == 1:
            res += 1

        res_list[b_pos] -= 1
        res_list[n_pos] += 1
        pos_dic[A_list[1]] = n_pos