A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

a_sum = sum(A_list)
b_sum = sum(B_list)
print(a_sum - b_sum + 1)