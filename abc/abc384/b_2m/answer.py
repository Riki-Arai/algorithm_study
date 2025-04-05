N, R = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

for A_list in A_lists:
    D, A = A_list
    if D == 1 and 1600 <= R <= 2799:
        R += A
    elif D == 2 and 1200 <= R <= 2399:
        R += A

print(R)