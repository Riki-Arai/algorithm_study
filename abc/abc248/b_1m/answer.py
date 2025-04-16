A, B, K = map(int, input().split())

res = 0
while A < B:
    res += 1
    A *= K

print(res)
