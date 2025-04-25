H, W = map(int, input().split())
A_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
B_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

a_lists, b_lists = [], []
for i in range(H):
    for j in range(W):
        if A_lists[i][j] == "#":
            a_lists.append((i, j))
        if B_lists[i][j] == "#":
            b_lists.append((i, j))

for i in range(H):
    for j in range(W):
        res_list = []
        for x in a_lists:
            res_list.append(((x[0]+i)%H, (x[1]+j)%W))

        if set(res_list) == set(b_lists):
            print("Yes")
            exit()

print("No")