X, A, D, N = map(int, input().split())

X -= A
e = (N-1)*D
if D >= 0:
    if X <= 0:
        print(abs(X))
    elif X >= e:
        print(abs(X-e))
    else:
        print(min(abs(X-X//D*D), abs(X-(X-(D-1))//D*D)))
else:
    if X >= 0:
        print(abs(X))
    elif X <= e:
        print(abs(e-X))
    else:
        print(min(abs(X-X//D*D), abs(X-(X-(D-1))//D*D)))