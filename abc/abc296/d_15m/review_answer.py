N, M = map(int, input().split())

res = float("INF")
for a in range(1, 10**6+1):
    if a > N:
        break
    tmp_b = M//a
    for i in range(10):
        b = i + tmp_b
        if b > N:
            break
        if a*b >= M:
            res = min(a*b, res)

if res == float("INF"):
    print(-1)
else:
    print(res)