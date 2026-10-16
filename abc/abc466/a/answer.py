N = int(input()) # 数値：1
X_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

for x in X_list:
    if x >= 0:
        print("No")
        exit()

print("Yes")