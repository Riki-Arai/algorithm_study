N = int(input())
S = input().strip()

dp = [[0, 0] for _ in range(N + 1)]

for r in range(1, N + 1):
    if S[r - 1] == '0':
        dp[r][0] = dp[r - 1][1]
        dp[r][1] = dp[r - 1][0] + 1
    else:
        dp[r][0] = dp[r - 1][0] + 1
        dp[r][1] = dp[r - 1][1]

ans = 0
for r in range(1, N + 1):
    ans += dp[r][0]

print(ans)