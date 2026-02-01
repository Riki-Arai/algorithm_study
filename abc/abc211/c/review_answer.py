s = input().strip()
t = "chokudai"

mod = 10**9 + 7
# dp[j]: 文字列 t の先頭 j 文字を作る方法の数
dp = [0]*(len(t)+1)
dp[0] = 1  # 空文字を作る方法は1通り

for c in s:
    # t の末尾から前へ更新していくのがポイント
    for j in range(len(t)-1, -1, -1):
        if c == t[j]:
            dp[j+1] = (dp[j+1] + dp[j]) % mod

print(dp[len(t)])

s = input().strip()

n = len(s)
t = "chokudai"
m = len(t)
mod = 10**9 + 7
# dp[i][j]: sの先頭i文字を使って tの先頭j文字を作る方法の数
dp = [[0]*(m+1) for _ in range(n+1)]
# 空文字同士をマッチさせる方法は1通り
for i in range(n+1):
    dp[i][0] = 1
# 漸化式
for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            # s[i]がt[j]と一致する場合は、「採用しない場合 + 採用する場合」
            dp[i+1][j+1] = (dp[i][j+1] + dp[i][j]) % mod
        else:
            # s[i]がt[j]と一致しない場合は「採用しない場合」のみ
            dp[i+1][j+1] = dp[i][j+1]

print(dp[n][m])