N = int(input()) # 数値：1
S_list = [input() for _ in range(N)] # 取得例：["A","B"・・・"E"]、N行の入力用
X, Y = input().split()

if S_list[int(X)-1] == Y:
    print("Yes")
else:
    print("No")