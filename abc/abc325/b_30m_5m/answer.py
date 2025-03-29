N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res_list = []
for i in range(0, 24):
    res = 0
    for A_list in A_lists:
        local_time = (i + A_list[1]) % 24
        if 9 <= local_time <= 17:
            res += A_list[0]
    res_list.append(res)

print(max(res_list))