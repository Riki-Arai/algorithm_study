n, a, b = map(int, input().split()) # 取得例：1 2

MOD = 10**9+7
def nCr_MOD(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    num = 1
    den = 1
    for i in range(r):
        num = (num * (n - i)) % MOD
        den = (den * (i + 1)) % MOD
    return (num * pow(den, MOD - 2, MOD)) % MOD

print((pow(2, n, MOD)-nCr_MOD(n, a)-nCr_MOD(n, b)-nCr_MOD(n, 0))%MOD)