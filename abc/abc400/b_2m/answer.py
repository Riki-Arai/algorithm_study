N, M = map(int, input().split()) # 取得例：1 2

res = 0
for i in range(M+1):
    res += N**i
    if res > 10**9:
        print("inf")
        exit()

print(res)