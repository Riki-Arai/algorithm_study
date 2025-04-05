H, W = map(int, input().split())
A_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

res_list = []
trans_A_lists = [list(row) for row in zip(*A_lists)]
for A_list in trans_A_lists:
    res_list.append(A_list.count("#"))

print(*res_list)