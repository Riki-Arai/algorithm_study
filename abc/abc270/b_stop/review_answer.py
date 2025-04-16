x, y, z = map(int, input().split())

def f(a, b, p):
    if b < a:
        a, b = b, a
    return a < p < b

ans = -1
if f(0, x, y):
    if f(0, z, y):
        ans = -1
    else:
        ans = abs(z) + abs(z - x)
else:
    ans = abs(x)

print(ans)