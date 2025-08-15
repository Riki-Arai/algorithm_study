N, K = map(int, input().split()) # 取得例：1 2

if 2*N> K:
    m = N//K
    print(min(abs(N-m*K), abs(N-(m+1)*K)))
else:
    print(N)