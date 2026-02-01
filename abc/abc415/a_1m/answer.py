N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
X = int(input()) # 数値：1

if X in A_list:
    print("Yes")
else:
    print("No")