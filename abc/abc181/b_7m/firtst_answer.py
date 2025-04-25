N = int(input()) # 取得例：1
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
for A_list in A_lists:
    a, b = A_list[0], A_list[1]
    res += (b*(b+1))/2 - ((a-1)*a)/2

print(int(res))