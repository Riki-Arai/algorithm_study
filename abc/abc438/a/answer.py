D, F = map(int, input().split()) # 取得例：1 2

for _ in range(10**6):
    F += 7
    if F > D:
        print(F%D)
        exit()