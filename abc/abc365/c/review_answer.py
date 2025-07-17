# リストではない場合の二分探索ではめぐる式を使用する
# ただし答えが必ず存在することが前提っぽく、答えが存在しない場合でもそれっぽい値を導出してしまう点に注意
# ちなみに計算量の見積もりもポイント
N, M = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

sum_ = sum(A_list)
if sum_ <= M:
    print("infinite")
    exit()

A_list.sort()
def is_ok(n):
    sum_ = 0
    for a in A_list:
        if a >= n:
            sum_ += n
        else:
            sum_ += a
    if sum_ <= M:
        return True
    return False  # 最小値の場合は>、>=を使用する。最大値の場合は逆の条件となる。

ok, ng = 0, 10**9+1  # 探索範囲の+1 or -1にしたものを指定。okが右側なら最小値、左側なら最大値を導出（例の値は最小値の場合）。
while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
    mid = (ok + ng) // 2
    # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)