N, M = map(int, input().split()) # 取得例：1 2
S_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

res_list = [0]*N
for j in range(M):
    one_num, zero_num = 0, 0
    tmp_res_list = [False]*N
    for i in range(N):
        if S_lists[i][j] == "1":
            tmp_res_list[i] = True
            one_num += 1
        else:
            zero_num += 1

    if one_num == N or zero_num == N:
        for k in range(N):
            res_list[k] += 1
    elif one_num > zero_num:
        for k, res in enumerate(tmp_res_list):
            if not res:
                res_list[k] += 1
    elif one_num < zero_num:
        for k, res in enumerate(tmp_res_list):
            if res:
                res_list[k] += 1

final_res_list = []
max_v = max(res_list)
for i, res in enumerate(res_list, 1):
    if res == max_v:
        final_res_list.append(i)

print(*final_res_list)