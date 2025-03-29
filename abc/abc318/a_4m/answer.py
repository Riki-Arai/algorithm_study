N, M, P = map(int, input().split())

res = 0
while M <= N:
    res += 1
    M += P

print(res)