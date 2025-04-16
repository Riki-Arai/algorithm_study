N, S, M, L = map(int, input().split())

res = 100**10
for i in range(100, -1, -1):
    for j in range(100, -1, -1):
        for k in range(100, -1, -1):
            eggs = i * 6 +  j * 8 + k * 12
            if eggs >= N:
                res = min(res, S*i+M*j+L*k)

print(res)