X, A, D, N = map(int, input().split())

if A < 0:
    A -= A
    X -= A

e = A+(N-1)*D
if X <= A:
    print(abs(A-X))
else:
    if A < X < e:
        print(X-(((X-A)//D)*D+A))
    else:
        print(X-e)