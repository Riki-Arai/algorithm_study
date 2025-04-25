N = int(input()) # 取得例：1
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
for A_list in A_lists:
    for B_list in A_lists:
        if A_list != B_list:
            x, y = A_list[0], A_list[1]
            xx, yy = B_list[0], B_list[1]
            if -1 <= (y - yy) / (x - xx) <= 1:
                res += 1

print(res//2)