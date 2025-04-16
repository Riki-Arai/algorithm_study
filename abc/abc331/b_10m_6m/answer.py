N, S, M, L = map(int, input().split())

res = float("INF")
for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            if i*6 + j*8 + k*12 >= N:
                res = min(res, S*i+M*j+L*k)

print(res)