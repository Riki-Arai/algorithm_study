N = int(input())

if len(str(N)) == 1:
    print((1+N)*N//2)
    exit()

res = 0
for d in range(1, len(str(N))):
    s = 10**(d-1)
    e = 9
    if d > 1:
        e = int("9"*d)
    res = (res + (e-s+1)*(1+(e-s+1))//2)%998244353

d = len(str(N))
s = 1
e = N-e
res = (res + (e-s+1)*(s+e)//2)%998244353
print(res)