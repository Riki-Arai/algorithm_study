N, L = map(int, input().split()) # 取得例：1 2

base = 0
for i in range(1, N+1):
    base += L+i-1

diff = float("INF")
for i in range(1, N+1):
    if diff > abs(L+i-1):
        res = base-(L+i-1)
        diff = abs(L+i-1)

print(res)