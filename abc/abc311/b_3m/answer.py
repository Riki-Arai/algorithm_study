N, D = map(int, input().split())
A_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

tmp_res, res = 0, 0
trans_A_lists = [list(row) for row in zip(*A_lists)]
for x_list in trans_A_lists:
    if len(set(x_list)) == 1 and "o" in set(x_list):
        tmp_res += 1
    else:
        res = max(res, tmp_res)
        tmp_res = 0

res = max(res, tmp_res)
print(res)