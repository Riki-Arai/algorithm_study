N, M, K = map(int, input().split())

dp_lists = [[0]*(K+1) for _ in range(N)]
for j in range(1, M+1):
    dp_lists[0][j] = 1

MOD = 998244353
for i in range(1, N):
    for j in range(K, 0, -1):
        if dp_lists[i-1][j] > 0:
            for m in range(M, 0, -1):
                if j+m <= K:
                    dp_lists[i][j+m] = (dp_lists[i][j+m]+dp_lists[i-1][j])%MOD

res = 0
for j in range(K+1):
    res = (res+dp_lists[N-1][j])%MOD

print(res)