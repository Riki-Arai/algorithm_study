N, K = map(int, input().split()) # 取得例：1 2

MOD = 10**9+7
res = 0
for k in range(K, N+2):
    min_v = ((k-1)*k//2)%MOD
    max_v = (((N+(N-k+1)))*k//2)%MOD
    res = (res + max_v-min_v+1)%MOD

print(res)