N = int(input()) # 取得例：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
for a, b in zip(A_list, B_list):
    res += a * b

if res == 0:
    print("Yes")
else:
    print("No")
