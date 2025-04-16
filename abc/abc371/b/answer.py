N, M = map(int, input().split())
A_lists = [input().split() for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

res_list = [False] * N
for A_list in A_lists:
    a, b = int(A_list[0]), A_list[1]
    if b == "M" and res_list[a-1] == False:
        print("Yes")
        res_list[a-1] = True
    else:
        print("No")