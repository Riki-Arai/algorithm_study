N, X = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

print(sum([a for a in A_list if a <= X]))