A_lists = [list(map(int, input().split())) for _ in range(3)] # 取得例:[[1,2], [3,4]・・[9,10]]
N = int(input()) # 取得例：1

res_lists = []
for _ in range(N):
    n = int(input())
    for i in range(3):
        for j in range(3):
            if A_lists[i][j] == n:
                res_lists.append((i, j))
                A_lists[i][j] = True

if set((0, 0), (1, 1), (1, 0)) <= set(res_lists):
    print("Yes")
    exit()