N, K = map(int, input().split()) # 取得例：1 2
input_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]、空白区切りの数値入力

input_lists.sort(lambda x: x[1])
def is_ok(n):
    count = 1
    i = 1
    r = input_lists[0][1]
    while i < N:
        if r+n <= input_lists[i][0]:
            count += 1
            r = input_lists[i][1]
        i += 1
    return count >= K

ok, ng = 0, 10**9+1  # 最大値を導出する場合は左側で確実にTrueとなる初期値を選択する。ただし例えばngの値を大きくしすぎると最大値が問題の閾値外になってしまうことがあるので注意。
while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
    mid = (ok + ng) // 2
    # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

if ok == 0:
    print(-1)
else:
    print(ok)