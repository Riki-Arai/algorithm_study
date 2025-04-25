N, S, D = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

for A_list in A_lists:
    x, y = A_list
    if x < S and y > D:
        print("Yes")
        exit()

print("No")