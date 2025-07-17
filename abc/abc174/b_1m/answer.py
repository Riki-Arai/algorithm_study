N, D = map(int, input().split()) # 取得例：1 2
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
for A_list in A_lists:
    x, y = A_list
    if x*x + y*y <= D*D:
        res += 1

print(res)