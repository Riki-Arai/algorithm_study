S_list = [input() for _ in range(3)] # 取得例：[A1、A2・・・An]、N行の入力用

res_list = ["ABC", "ARC", "AGC", "AHC"]
for s in S_list:
    res_list.remove(s)

print(res_list[0])