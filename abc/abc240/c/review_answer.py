N, X = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

# dp[s] = True なら、「ある時点で位置 s に到達可能」
dp = [False] * (10000 + 1)
dp[0] = True  # ジャンプ前、位置 0 にいる
for (a, b) in AB:
    new_dp = [False] * (10000 + 1)
    for pos in range(10000 + 1):
        if not dp[pos]:
            continue
        # このジャンプで a を使う
        if pos + a <= 10000:
            new_dp[pos + a] = True
        # このジャンプで b を使う
        if pos + b <= 10000:
            new_dp[pos + b] = True
    dp = new_dp

print("Yes" if dp[X] else "No")
