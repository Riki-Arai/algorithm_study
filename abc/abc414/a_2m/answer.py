N, L, R = map(int, input().split()) # 取得例：1 2
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
for x, y in A_lists:
    if x <= L and R <= y:
        res += 1

print(res)