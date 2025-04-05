Q = int(input())
A_lists = [list(map(int, input().split())) for _ in range(Q)] # 取得例:[[1,2], [3,4]・・[9,10]]

res_list = [0] * 100
for A_list in A_lists:
    if len(A_list) == 1:
        print(res_list.pop(-1))
    else:
        res_list.append(A_list[1])