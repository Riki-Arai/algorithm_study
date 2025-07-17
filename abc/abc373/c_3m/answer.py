N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

A_list.sort(reverse=True)
B_list.sort(reverse=True)
print(A_list[0] + B_list[0])