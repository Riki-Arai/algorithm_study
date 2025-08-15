X, A, D, N = map(int, input().split())

# dが負なら数列が単調増加になるように調整(常にAを左側になるようにしたい)
if D < 0:
    A = A + D*(N-1)
    D = -D

def is_ok(n):
    return A + D*n >= X

ok, ng = N, -1  # 探索範囲の+1 or -1にしたものを指定。okが右側なら最小値、左側なら最大値を導出（例の値は最小値の場合）。
while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
    mid = (ok + ng) // 2
    # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

res = float("INF")
# okは条件を満たす最小値であるだけで、Xと比較して距離の小さい値というわけではないので改めて求めている
# 例えばS = [2, 5, 8, 10]とあり、Xが6の場合だとok=2で8 >= 6となるが、最短距離であるわけではないので6に対して5・8を比較している
# なお最小値のok（インデックス）を求めており、ok+1の条件についてはむしろ距離が離れるため比較する必要がない
if 0 <= ok < N:
    res = min(res, abs((A + D*ok) - X))
if 0 <= ok - 1 < N:
    res = min(res, abs((A + D*(ok - 1)) - X))

print(res)