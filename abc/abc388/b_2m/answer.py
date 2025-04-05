N, D = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

for d in range(1, D+1):
    res_list = []
    for A_list in A_lists:
        res_list.append(A_list[0] * (A_list[1] + d))
    print(max(res_list))