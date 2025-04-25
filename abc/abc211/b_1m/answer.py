A_list = [input() for _ in range(4)] # 取得例：[A1、A2・・・An]、N行の入力用

res_list = ["H", "2B", "3B", "HR"]
for a in A_list:
    if a in res_list:
        res_list.remove(a)

if len(res_list) == 0:
    print("Yes")
else:
    print("No")