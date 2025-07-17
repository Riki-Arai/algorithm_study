N, X, Y = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

tate_list = []
for i in range(N):
    tate_list.append([A_list[i], B_list[i]])

tate_list.sort(key=lambda x: x[0], reverse=True)
limit_a, limit_b = 0, 0
tmp_res_1 = 0
for i in range(N):
    limit_a += tate_list[i][0]
    limit_b += tate_list[i][1]
    tmp_res_1 += 1
    if limit_a > X or limit_b > Y:
        break

tate_list.sort(key=lambda x: x[1], reverse=True)
limit_a, limit_b = 0, 0
tmp_res_2 = 0
for i in range(N):
    limit_a += tate_list[i][0]
    limit_b += tate_list[i][1]
    tmp_res_2 += 1
    if limit_a > X or limit_b > Y:
        break

print(min(tmp_res_1, tmp_res_2))