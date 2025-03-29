N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

max_v = max(A_list)
res_list = [a for a in A_list if a != max_v]
print(max(res_list))