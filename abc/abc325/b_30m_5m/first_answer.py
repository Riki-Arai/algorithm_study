N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
for t in range(0, 24):
    tmp_res = 0
    for A_list in A_lists:
        local_start_time = (t + A_list[1]) % 24
        if 9 <= local_start_time <= 17: 
            tmp_res += A_list[0]

    res = max(res, tmp_res)

print(res)