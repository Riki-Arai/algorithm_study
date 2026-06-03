N = int(input())

MOD = 998244353
d = len(str(N))
r = pow(10, d, MOD)
a = pow(r, N, MOD)-1
b = pow(r-1, -1, MOD)
res = a*b%MOD
print(res*N%MOD)