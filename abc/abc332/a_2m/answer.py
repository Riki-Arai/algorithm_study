N, S, K = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
for A_list in A_lists:
    res += A_list[0] * A_list[1]

if res >= S:
    print(res)
else:
    print(res+K)