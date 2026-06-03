H, W, N = map(int, input().split()) # 取得例：1 2
A_lists = [list(map(int, input().split())) for _ in range(H)] # 取得例:[[1,2], [3,4]・・[9,10]]
B_set = set(int(input()) for _ in range(N)) # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
for i in range(H):
    tmp_res = 0
    for j in range(W):
        if A_lists[i][j] in B_set:
            tmp_res += 1

    res = max(tmp_res, res)

print(res)