import math

R = int(input())

res = 0
for x in range(1, 10**6+1):
    def is_ok(n):
        return pow(0.5+n, 2)+pow(x+0.5, 2) <= R**2

    # okはここではy（高さ）
    ok, ng = 0, 10**9+1  # 最大値を導出する場合は左側で確実にTrueとなる初期値を選択する。ただし例えばngの値を大きくしすぎると最大値が問題の閾値外になってしまうことがあるので注意。
    while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
        mid = (ok + ng) // 2
        # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    res += ok

# R-1はx座標ory座標が0の時に円で囲む事ができる個数
# なぜR-1になるかは数式としても証明できるがx=0 or y=0で固定してRをいくつか値を変更して検証をしてみると、中心の正方形以外でR-1個含む事が確認できる
print(res*4+(R-1)*4+1)