N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [-float("inf")] * (M + 1)
dp[0] = 0
for a in A:
    for j in range(M, 0, -1):
        dp[j] = max(dp[j], dp[j-1] + j * a)

print(dp[M])