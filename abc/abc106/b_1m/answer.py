import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1

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
for i in range(1, N+1):
    if i%2 != 0 and len(divisors(i)) == 8:
        res += 1

print(res)