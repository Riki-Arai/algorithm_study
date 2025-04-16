N = int(input())
X_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

X_list.sort()
print(sum(X_list[N:-N])/(3*N))