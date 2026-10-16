N = int(input().strip())
p_list = list(map(float, input().split()))

# dp[j] = 表が j 枚出る確率（初期値：0枚の確率が 1.0）
dp = [1.0] + [0.0] * N
for p in p_list:
    # 後ろから更新することで、同じターンの更新結果を使い回さないようにする
    for j in range(N, 0, -1):
        dp[j] = dp[j] * (1.0 - p) + dp[j-1] * p
    # 0枚になる確率は裏が出続けるだけ
    dp[0] *= (1.0 - p)

# 答え：表が過半数（N // 2 + 1 枚以上）の確率を合計
print(f"{sum(dp[N // 2 + 1:]):.10f}")