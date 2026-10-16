N, K, D = map(int, input().split())

a = list(map(int, input().split()))

# dp[i][j][k]
# i個目まで見た時、j個選び、合計値のDでの余りがkの時の最大値
dp = [[[-1] * D for _ in range(K + 1)] for _ in range(N + 1)]

dp[0][0][0] = 0
for i in range(N):
    for j in range(K + 1):
        for k in range(D):
            if dp[i][j][k] == -1:
                continue

            # a_i を選ばない場合
            dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])

            # a_i を選ぶ場合
            if j != K:
                nk = (k + a[i]) % D
                dp[i + 1][j + 1][nk] = max(
                    dp[i + 1][j + 1][nk],
                    dp[i][j][k] + a[i]
                )

print(dp[N][K][0])