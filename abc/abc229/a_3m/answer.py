S_lists = [list(input()) for _ in range(2)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

res_list = []
for i in range(2):
    for j in range(2):
        if S_lists[i][j] == "#":
            res_list.append((i, j))

if res_list == [(0, 0), (1, 1)] or res_list == [(0, 1), (1, 0)]:
    print("No")
else:
    print("Yes")