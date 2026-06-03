import math

N = int(input())

res = 0
for a in range(1, 60):
    m = math.isqrt(N // (1 << a))
    res += (m + 1) // 2

print(res)