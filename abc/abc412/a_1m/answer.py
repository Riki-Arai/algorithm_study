N = int(input()) # 数値：1
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
for a, b in A_lists:
    if b > a:
        res += 1

print(res)