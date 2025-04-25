N = int(input()) # 数値
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

a = max(A_list)
b = min(B_list)
if b - a < 0:
    print(0)
else:
    print(b - a + 1)