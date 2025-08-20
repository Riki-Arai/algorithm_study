X, A, D, N = map(int, input().split())

# 後の二分探索の初期設定で矛盾が起きないようにDを必ず0以上にする（Aも常に左端にする）
if D < 0:
    A = A + D*(N-1)
    D *= -1

s = A
g = A + D*(N-1)
if X < s:
    print(abs(s-X))
elif X > g:
    print(abs(X-g))
else:
    def is_ok(n):
        return A+D*n >= X

    ok, ng = 10**18+1, -10**18-1  # 基本的にokはis_okの条件を必ずTrue、ngは必ずFalseで設定。ただし探索条件の中で最適を探りたい時は必ずTrue、Falseである必要はないケースもある。
    while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
        mid = (ok + ng) // 2
        # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    print(min(abs(X-(A+D*ok)), abs(X-(A+D*(ok-1)))))

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