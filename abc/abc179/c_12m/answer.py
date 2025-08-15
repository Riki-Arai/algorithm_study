N = int(input()) # 取得例：1

res = 0
for a in range(1, 10**6+1):
    for b in range(1, N//a+1):
        if N - a*b > 0:
            res += 1

print(res)