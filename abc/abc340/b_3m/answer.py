N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res_list = []
for A_list in A_lists:
    q = A_list[0]
    if q == 1:
        x = A_list[1]
        res_list.append(x)
    elif q == 2:
        k = A_list[1]
        print(res_list[-k])