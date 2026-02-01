N, R = map(int, input().split()) # 取得例：1 2
L_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res_lists = []
l_i , r_i = float("INF"), 0
for i in range(N):
    res_lists.append(["r", i, None])
    res_lists.append(["k", i, L_list[i]])
    if L_list[i] == 0:
        l_i = min(l_i, 2*i+1)
        r_i = max(r_i, 2*i+1)


res_lists.append(["r", N, None])
room_j = 0
for j, res_list in enumerate(res_lists):
    x, y, _ = res_list
    if x == "r" and y == R:
        room_j = j
        break

res = 0
if l_i >= room_j:
    for k in range(l_i, r_i):
        x, y, z = res_lists[k]
        if x == "k" and z == 0:
            res += 1
        elif x == "k" and z == 1:
            res += 2
else:
    for k in range(room_j, l_i-1, -1):
        x, y, z = res_lists[k]
        if x == "k" and z == 1:
            res_lists[k][2] = 0
            res += 1
    for k in range(l_i, r_i+1):
        x, y, z = res_lists[k]
        if x == "k" and z == 0:
            res += 1
        elif x == "k" and z == 1:
            res += 2

print(res)