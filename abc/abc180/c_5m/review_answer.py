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

for res in divisors(N):
    print(res)