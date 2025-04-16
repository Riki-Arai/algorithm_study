N, M, P = map(int, input().split())

res = 0
while M <= N:
    M += P
    res += 1

print(res)