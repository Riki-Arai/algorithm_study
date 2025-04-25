H, W = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(H)] # 取得例:[[1,2], [3,4]・・[9,10]]


for i in range(H):
    for j in range(W):
        for ii in range(i):
            for jj in range(j):
                if A_lists[i][j] + A_lists[ii][jj] <= A_lists[ii][j] + A_lists[i][jj]:
                    continue
                else:
                    print("No")
                    exit()

print("Yes")