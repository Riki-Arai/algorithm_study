X, K, D = map(int, input().split()) # 取得例：1 2

if X < 0:
    X *= -1

if D < X:
    m = X // D
    if m >= K:
        print(abs(X-K*D))
    else:
        K -= m
        if K % 2 == 0:
            print(abs(X-m*D))
        else:
            print(abs(X-(m+1)*D))
elif D == X:
    if K % 2 == 0:
        print(abs(X))
    else:
        print(0)
else:
    if K % 2 == 0:
        print(abs(X))
    else:
        print(abs(D-X))