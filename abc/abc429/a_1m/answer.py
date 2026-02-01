N, M = map(int, input().split()) # 取得例：1 2

for i in range(1, N+1):
    if i > M:
        print("Too Many Requests")
    else:
        print("OK")