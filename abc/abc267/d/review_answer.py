import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

# dp[i][j] を保持する 2D DP テーブル
# dp[i][j] = i 個選んだときの最大値 （最初は -∞）
dp = [[-10**18] * (m+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(1, n+1):
    for j in range(0, m+1):
        if j == 0:
            dp[i][0] = 0
        elif j > i:
            dp[i][j] = -10**18
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + a[i-1] * j)

print(dp[n][m])