A, B, X = map(int, input().split()) # 取得例：1 2

if A + B > X:
    print(0)
elif A*10**9 + B*10 <= X:
    print(10**9)
else:
    def is_ok(n):
        return A*n + B*len(str(n)) <= X

    ok, ng = 0, 10**9+1  # 最大値を導出する場合は左側で確実にTrueとなる初期値を選択する。ただし例えばngの値を大きくしすぎると最大値が問題の閾値外になってしまうことがあるので注意。
    while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
        mid = (ok + ng) // 2
        # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    print(ok)