N = int(input())
A_list = [input() for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用

res_list = []
for i, a in enumerate(A_list, 1):
    res_list.append([i, a.count("o")])

sorted_res_list = sorted(res_list, key=lambda x: x[1], reverse=True)
tmp_list = [] 
for res in sorted_res_list:
    tmp_list.append(res[0])

print(*tmp_list)