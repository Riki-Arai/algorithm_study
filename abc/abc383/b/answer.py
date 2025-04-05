H, W, D = map(int, input().split())
A_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

res_lists = []
for i in range(H):
    for j in range(W):
        if A_lists[i][j] == ".":
            res_list = []
            for k in range(H):
                for l in range(W):
                    if abs(i-k) + abs(j-l) <= D and A_lists[k][l] == ".":
                        res_list.append((k, l))
            res_lists.append(res_list)

res = 0
for i in res_lists:
    for j in res_lists:
        res = max(res, len(set(i + j)))

print(res)