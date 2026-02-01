N = int(input())

dp_lists = [[0]*10 for _ in range(N)]
for j in range(1, 10):
    dp_lists[0][j] = 1

for i in range(1, N):
    for j in range(1, 10):
        dp_lists[i][j] = dp_lists[i-1][j]%998244353
        if j-1 >= 0:
            dp_lists[i][j] = (dp_lists[i][j] + dp_lists[i-1][j-1])%998244353
        if j+1 <= 9:
            dp_lists[i][j] = (dp_lists[i][j] + dp_lists[i-1][j+1])%998244353

print(sum(dp_lists[N-1])%998244353)