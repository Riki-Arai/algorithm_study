N, Q = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

A_list.sort()
def is_ok(i, x):
    return A_list[i] >= x  # 最小値を求めたい場合の例。最大値の場合は i <= 5 のようになる。


for _ in range(Q):
    input_ = int(input())
    ok, ng = N, -1  # 探索範囲の+1 or -1にしたものを指定。okが右側なら最小値、左側なら最大値を導出（例の値は最小値の場合）。
    while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
        mid = (ok + ng) // 2
        # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
        if is_ok(mid, input_):
            ok = mid
        else:
            ng = mid

    print(N-ok)