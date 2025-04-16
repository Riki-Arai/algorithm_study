N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
grid_lists = [["."]*100 for _ in range(100)]

for a_list in A_lists:
    A, B, C, D = a_list[0], a_list[1], a_list[2], a_list[3]
    for i in range(A, B):
        for j in range(C, D):
            grid_lists[i][j] = "#"

res = 0
for grid_list in grid_lists:
    res += grid_list.count("#")

print(res)