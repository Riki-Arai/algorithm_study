N = int(input())

res = 0
s = 0
m = 0
while s < N:
    m += 1
    s += m
    res += 1

print(res)
