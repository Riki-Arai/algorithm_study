X, Y, N = map(int, input().split())

x = X*N
xy = Y*(N // 3) + X*(N % 3)
print(min(x, xy))


### 以下はfirst
#X, Y, N = map(int, input().split())
#
#if 3 * X > Y:
#    print(Y*(N // 3) + X*(N % 3))
#elif 3 * X <= Y:
#    print(X*N)