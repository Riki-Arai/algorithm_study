N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

for A_list in A_lists:
    res_list = []
    for i, a in enumerate(A_list, 1):
        if a == 1:
            res_list.append(i)

    print(*res_list)