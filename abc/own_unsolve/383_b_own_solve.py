H, W, D = map(int, input().split())
s_list = [input() for _ in range(H)]

res_dic = {}
for i in range(H):
    for j in range(W):
        if s_list[i][j] == ".":
            res_list = []
            for k in range(H):
                for l in range(W):
                    if abs(i-k)+abs(j-l) <= D and s_list[k][l] == ".":
                        res_list.append((k, l))
            res_dic[(i, j)] = set(res_list)

res_list = []
for i in res_dic:
    for j in res_dic:
        res_list.append(len(res_dic[i] | res_dic[j]))

print(max(res_list))
