N, M, T = map(int, input().split()) # 取得例：1 2
A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

rem = N
last_time = 0
for A_list in A_lists:
    rem -= (A_list[0] - last_time)
    if rem <= 0:
        print("No")
        exit()
    rem = min(N, rem + A_list[1] - A_list[0])
    last_time = A_list[1]

if rem - (T - last_time) > 0:
    print("Yes")
else:
    print("No")