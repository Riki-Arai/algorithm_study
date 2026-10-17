
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
P = list(map(int, input().split()))

INF = 10**30

# dp[i][j] = マス (i, j) に到着した時点で必要な最小コイン数
dp = [[INF] * W for _ in range(H)]

for i in range(H - 1, -1, -1):
    for j in range(W - 1, -1, -1):
        # このマスで回収・消費するコイン数
        gain = A[i][j] - P[i + j]

        if i == H - 1 and j == W - 1:
            # ゴールでは、このマスの収支を処理できればよい
            dp[i][j] = max(0, -gain)
        else:
            need = INF

            # 右へ移動
            if j + 1 < W:
                need = min(need, dp[i][j + 1])

            # 下へ移動
            if i + 1 < H:
                need = min(need, dp[i + 1][j])

            # このマスの収支を反映する前に必要なコイン数
            dp[i][j] = max(0, need - gain)

print(dp[0][0])
