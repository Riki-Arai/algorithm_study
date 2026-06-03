A, B = map(int, input().split()) # 取得例：1 2

m = 1
res = 0
for i in range(10**7):
    if m >= B:
        print(res)
        exit()
    m -= 1
    m += A
    res += 1