N = int(input())
A_list = [input() for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用

A_list.sort(key=lambda x: len(x))
print("".join(A_list))