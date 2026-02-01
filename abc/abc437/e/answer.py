N = int(input()) # 数値：1
T_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res_lists = []
for i, t in enumerate(T_list, 1):
    res_lists.append([t, i])

res_lists.sort()
res_list = []
for i in range(3):
    res_list.append(res_lists[i][1])

print(*res_list)