import bisect as bi

N, Q = map(int, input().split())
A_list = list(map(int, input().split()))

for _ in range(Q):
    K = int(input())

    def is_ok(n):
        b_i = bi.bisect_right(A_list, n)
        return n-b_i >= K

    ok, ng = 2*10**18+1, 0  # 最大値を導出する場合は左側で確実にTrueとなる初期値を選択する。ただし例えばngの値を大きくしすぎると最大値が問題の閾値外になってしまうことがあるので注意。
    while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
        mid = (ok + ng) // 2
        # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    print(ok)