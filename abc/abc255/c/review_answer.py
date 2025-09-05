X, A, D, N = map(int, input().split())

if D < 0:
    s = A
    g = A + D*(N-1)
    s, g = g, s
    D *= -1
else:
    s = A
    g = A + D*(N-1)

if g <= X:
    print(abs(X-g))
elif X <= s:
    print(abs(s-X))
else:
    def is_ok(n):
        return s+n*D > X

    ok, ng = N, 0  # 最大値を導出する場合は左側で確実にTrueとなる初期値を選択する。ただし例えばngの値を大きくしすぎると最大値が問題の閾値外になってしまうことがあるので注意。
    while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
        mid = (ok + ng) // 2
        # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    print(min(abs(X-(s+ok*D)), abs(X-(s+(ok-1)*D))))

# first
#x, a, d, n = map(int, input().split())
#
## dが負なら初項を末項にし、公差を正に変換
#if d < 0:
#    a = a + d * (n - 1)
#    d = -d
#
#st = a
#fi = a + d * (n - 1)
#if x < st:
#    print(st - x)
#elif x > fi:
#    print(x - fi)
#else:
#    # Xが数列の範囲内 => D の倍数に丸める距離を算出
#    if d == 0:
#        # 公差が0ならすべて同じ値
#        print(abs(x - a))
#    else:
#        r = (x - st) % d
#        # 2つの項の間にある場合で左側 or 右側のどちらからの方が近いを導出している
#        print(min(r, d - r))