H, W = map(int, input().split())
A_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

res_lists = []
for i in range(H):
    for j in range(W):
        if A_lists[i][j] == "o":
            res_lists.append([i, j])

print(abs(res_lists[0][0]-res_lists[1][0]) + abs(res_lists[0][1]-res_lists[1][1]))