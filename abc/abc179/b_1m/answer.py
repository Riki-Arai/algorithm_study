N = int(input()) # 取得例：1
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

count = 0
for A_list in A_lists:
    if A_list[0] == A_list[1]:
        count += 1
        if count == 3:
            print("Yes")
            exit()
    else:
        count = 0

print("No")