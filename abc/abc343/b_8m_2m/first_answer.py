N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

for i in range(N):
    res_list = []
    for j in range(N):
        if A_lists[i][j] == 1:
            res_list.append(j+1)
    print(*res_list)