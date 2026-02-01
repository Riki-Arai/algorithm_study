X, K, D = map(int, input().split())
X = abs(X)
q, r = divmod(X, D)  # XをDで割った商 q と余り r
if q >= K:
    # K回移動しても余りがまだ残る(または丁度K回で到達)
    print(X - D*K)
else:
    rem = K - q
    # 残りの移動回数 rem が偶数か奇数かで最終地点が変わる
    if rem % 2 == 0:
        print(r)
    else:
        print(D - r)

## first
#X, K, D = map(int, input().split()) # 取得例：1 2
#
#if X < 0:
#    X *= -1
#
#if D < X:
#    m = X // D
#    if m >= K:
#        print(abs(X-K*D))
#    else:
#        K -= m
#        if K % 2 == 0:
#            print(abs(X-m*D))
#        else:
#            print(abs(X-(m+1)*D))
#elif D == X:
#    if K % 2 == 0:
#        print(abs(X))
#    else:
#        print(0)
#else:
#    if K % 2 == 0:
#        print(abs(X))
#    else:
#        print(abs(D-X))