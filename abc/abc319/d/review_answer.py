N, M = map(int, input().split())
L_list = list(map(int, input().split()))

def is_ok(n):
    line = 1
    w_n = 0
    for l in L_list:
        if w_n == 0:
            w_n = l
            continue

        if line >= M and w_n > n:
            return False

        if w_n+l+1 <= n:
            w_n += l+1
        else:
            line += 1
            w_n = l

    return line <= M

ok, ng = 10**18+1, 0  # 最大値を導出する場合は左側で確実にTrueとなる初期値を選択する。ただし例えばngの値を大きくしすぎると最大値が問題の閾値外になってしまうことがあるので注意。
while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
    mid = (ok + ng) // 2
    # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)