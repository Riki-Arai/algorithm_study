import bisect as bi

N, Q = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res_list = []
A_list.sort()
for _ in range(Q):
    X, Y = map(int, input().split()) # 取得例：1 2
    b_i = bi.bisect_left(A_list, X)

    def is_ok(n, b_i):
        bb_i = bi.bisect_left(A_list, n, b_i)
        return n-(X)-(bb_i-b_i) >= Y

    ok, ng = 2*10**9+1, 0  # 最大値を導出する場合は左側で確実にTrueとなる初期値を選択する。ただし例えばngの値を大きくしすぎると最大値が問題の閾値外になってしまうことがあるので注意。
    while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
        mid = (ok + ng) // 2
        # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
        if is_ok(mid, b_i):
            ok = mid
        else:
            ng = mid

    res_list.append(ok-1)

for res in res_list:
    print(res)