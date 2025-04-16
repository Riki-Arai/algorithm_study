N, T = map(int, input().split())
C_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
R_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = []
for i, c in enumerate(C_list):
    if c == T:
        res_list.append([i+1, R_list[i]])

if len(res_list) > 0:
    res_list.sort(key=lambda x: x[1], reverse=True)
    print(res_list[0][0])
else:
    for i, c in enumerate(C_list):
        if c == C_list[0]:
            res_list.append([i+1, R_list[i]])
    res_list.sort(key=lambda x: x[1], reverse=True)
    print(res_list[0][0])