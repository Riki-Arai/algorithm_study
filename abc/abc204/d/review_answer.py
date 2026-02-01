# 部分話問題に着地するのがポイント
T = list(map(int, input().split()))
S = sum(T)

dp = [False] * (S + 1)
dp[0] = True
for t in T:
    for i in range(S, t - 1, -1):
        if dp[i - t]:
            dp[i] = True

ans = S
# 部分話を総当たりするともう片方の時間が求められるので、双方を比較した時の最大値が作業時間となる
for i in range(S + 1):
    if dp[i]:
        ans = min(ans, max(i, S - i))

print(ans)