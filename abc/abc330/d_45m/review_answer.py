from collections import defaultdict

N = int(input())
g_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

v_dict, w_dict = defaultdict(int), defaultdict(int)
for i in range(N):
    for j in range(N):
        if g_lists[i][j] == "o":
            v_dict[j] += 1
            w_dict[i] += 1

res = 0
for i in range(N):
    for j in range(N):
        if g_lists[i][j] == "o":
            if v_dict[j] >= 2 and w_dict[i] >= 2:
                v_v = v_dict[j]
                w_v = w_dict[i]
                res = res + (v_v-1) * (w_v-1)

print(res)