S = input().strip()

MOD = 998244353
dp_lists = [[0] * (len(S)+1) for _ in range(len(S)+1)]
dp_lists[0][0] = 1
for i in range(len(S)):
    s = S[i]
    if s != ")":
        for j in range(len(S)-1):
            dp_lists[i+1][j+1] = (dp_lists[i+1][j+1] + dp_lists[i][j])%MOD
    if s != "(":
        for j in range(1, len(S)):
            dp_lists[i+1][j-1] = (dp_lists[i+1][j-1] + dp_lists[i][j])%MOD

print(dp_lists[len(S)][0])

MOD = 998244353

s = input().strip()
n = len(s)

dp = [[0] * (n + 1) for _ in range(n + 1)]
# 値はその列に至るまでの経路。空文字に至る経路は当然ながら1となる。
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if s[i] != ')':
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
        if s[i] != '(' and j > 0:
            dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD

print(dp[n][0])