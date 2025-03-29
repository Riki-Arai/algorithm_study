import math

N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

for a_list in A_lists:
    res_list = []
    x = a_list[0]
    y = a_list[1]
    for b_list in A_lists:
        xx = b_list[0]
        yy = b_list[1]
        res_list.append(math.sqrt(pow(x-xx, 2) + pow(y-yy, 2)))

    max_dis = max(res_list)
    print(res_list.index(max_dis)+1)