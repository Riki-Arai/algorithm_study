N, X = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

A_list = [a-1 if i % 2 == 0 else a for i, a in enumerate(A_list, 1)]
if sum(A_list) <= X:
    print("Yes")
else:
    print("No")