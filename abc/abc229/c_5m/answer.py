N, W = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
A_lists.sort(key=lambda x: x[0], reverse=True)
for a, b in A_lists:
    if W - b < 0:
        res += a*W
        break
    else:
        res += a*b
        W -= b

print(res)