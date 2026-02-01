n, m, k = map(int, input().split())

mod = 998244353
# dp[x][y] : x 回の操作で合計 y になる方法数
dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 1
for x in range(1, n + 1):
    for y in range(k + 1):
        now = 0
        for i in range(1, m + 1):
            if y - i >= 0:
                now += dp[x - 1][y - i]
                now %= mod
        dp[x][y] = now

ans = 0
for y in range(k + 1):
    ans += dp[n][y]
    ans %= mod

print(ans)