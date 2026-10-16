N = int(input())

MOD = 998244353
d = len(str(N))
a = pow(10**d, N, MOD)-1
b = pow(pow(10, d, MOD)-1, -1, MOD)
# 掛け算の形にしないと和が合わなくなるので注意
res = a*b%MOD
print(res*N%MOD)