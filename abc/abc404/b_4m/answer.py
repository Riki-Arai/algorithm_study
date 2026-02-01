N = int(input()) # 数値：1
S_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解
T_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

res = 0
for i in range(N):
    for j in range(N):
        if S_lists[i][j] != T_lists[i][j]:
            res += 1

for i in range(1, 4):
    tmp_res = i
    S_lists = [list(reversed(items)) for items in zip(*S_lists)] # 90度右回転
    for i in range(N):
        for j in range(N):
            if S_lists[i][j] != T_lists[i][j]:
                tmp_res += 1

    res = min(tmp_res, res)

print(res)