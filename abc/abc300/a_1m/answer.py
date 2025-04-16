N, A, B = map(int, input().split())
C_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

print(C_list.index(A+B)+1)