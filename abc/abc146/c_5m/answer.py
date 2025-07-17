A, B, X = map(int, input().split()) # 取得例：1 2

ok = 0
ng = 10**9 + 1
def is_ok(i):
    if A*i + B*len(str(i)) <= X:
        return True
    return False

while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
    mid = (ok + ng) // 2
    # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)