X, Y, Z = map(int, input().split())

def f(a, b, p):
    if a > b:
        a, b = b, a
    return a < p < b

if f(0, Y, X):
    print(abs(X))
else:
    if f(0, Z, Y):
        print(-1)
    else:
        print(abs(Z) + abs(X-Z))