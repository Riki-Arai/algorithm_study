N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

dp_lists = [[0]*(3001) for _ in range(N)]
for i in range(0, 3001):
    if A_list[0] <= i <= B_list[0]:
        dp_lists[0][i] = dp_lists[0][i-1] + 1
    else:
        dp_lists[0][i] = dp_lists[0][i-1]

for i in range(1, N):
    a, b = A_list[i], B_list[i]
    for j in range(3001):
        if j == a:
            dp_lists[i][j] = dp_lists[i-1][j]
        elif a < j <= b:
            # dp_lists[i-1][j]はi-1でj以下のパターン数なので、jを追加することで新しく追加できるパターン数
            dp_lists[i][j] = (dp_lists[i-1][j] + dp_lists[i][j-1])%998244353
        else:
            dp_lists[i][j] = dp_lists[i][j-1]

print(dp_lists[N-1][3000])