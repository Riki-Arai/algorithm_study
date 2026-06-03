N = int(input()) # 数値：1
X_lists = [list(map(int, input().split())) for _ in range(3)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
for i in range(N):
    a = X_lists[0][i]-1
    if i == 0:
        res += X_lists[1][a]
    else:
        pre_a = X_lists[0][i-1]-1
        if pre_a+1 == a:
            res += (X_lists[1][a]+X_lists[2][pre_a])
        else:
            res += X_lists[1][a]

print(res)