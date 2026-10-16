X, Y = map(int, input().split()) # 取得例：1 2

MOD = 10**9 + 7
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

res = 0
for i in range(X//2+1):
    if i == 0 and 2*X == Y:
        res = (res + 1)%MOD
    elif i == X and X%2 == 0 and X//2 == Y:
        res = (res + 1)%MOD
    elif 0 < i < X and (X-2*i)*2 + i == Y:
        res = (res + nCr_MOD(X-2*i+i, i))%MOD

print(res)