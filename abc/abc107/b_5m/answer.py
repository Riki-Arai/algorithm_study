import sys; sys.setrecursionlimit(10**7)

H, W = map(int, input().split()) # 取得例：1 2
g_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

ng_h_set = set()
for i in range(H):
    for j in range(W):
        if g_lists[i][j] == "#":
            break
    else:
        ng_h_set.add(i)

ng_w_set = set()
for j in range(W):
    for i in range(H):
        if g_lists[i][j] == "#":
            break
    else:
        ng_w_set.add(j)

res_lists = []
for i in range(H):
    if i in ng_h_set:
        continue
    tmp_res_list = []
    for j in range(W):
        if j in ng_w_set:
            continue
        tmp_res_list.append(g_lists[i][j])
    res_lists.append(tmp_res_list)

for res_list in res_lists:
    print("".join(res_list))