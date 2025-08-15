N = int(input()) # 数値：1

res = float("INF")
for a in range(1, 10**6+1):
    if N % a == 0:
        b = N/a
        res = min(a-1+b-1, res)

print(int(res))