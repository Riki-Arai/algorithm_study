A, B = map(int, input().split())

res = float("INF")
x = int(pow(A/(2*B), 2/3) - 1)
for i in range(-10, 11, 1):
    xx = x + i
    if xx >= 0:
        res = min(B*xx + A/pow(1+xx, 1/2), res)

print(res)
