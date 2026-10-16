N = int(input())

def divisors(n: int) -> list:
    res = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            if i * i != n:
                res.append(n // i)
        i += 1
    res.sort()
    return res

res = 0
for d in divisors(2*N):
    if (d%2 == 0 and (2*N//d)%2 == 1) or (d%2 == 1 and (2*N//d)%2 == 0):
        res += 1

print(res)