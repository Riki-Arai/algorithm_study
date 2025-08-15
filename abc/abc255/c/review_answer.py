X, A, D, N = map(int, input().split())

# dが負なら数列が単調増加になるように調整
if D < 0:
    A = A + D*(N-1)
    D = -D

ng = -1
ok = N
while ok - ng > 1:
    mid = (ok + ng) // 2
    if A + D*mid >= X:
        ok = mid
    else:
        ng = mid

# ok が「a + d*ok >= x となる最小のインデックス」になる
# 周囲のインデックスを確認して最小距離を求める
res = float("INF")
if 0 <= ok < N:
    res = min(res, abs((A + D*ok) - X))
if 0 <= ok - 1 < N:
    res = min(res, abs((A + D*(ok - 1)) - X))

print(res)

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