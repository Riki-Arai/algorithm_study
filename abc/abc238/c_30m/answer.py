N = int(input())

d = len(str(N))
res = 0
for i in range(d-1):
    res += 9*10**i*(9*10**i+1)//2

m = (N-(1*10**(d-1)))+1
res += m*(m+1)//2
print(res%998244353)
