N = int(input())

if N == 0:
    print(0)
    exit()

def calc(a, b):
    return a**3+a**2*b+a*b**2+b**3

def is_ok(a, b):
    return calc(a, b) >= N

res = float("INF")
for a in range(10**6+1):
    ok, ng = 10**6+1, -1  # 最大値を導出する場合は左側で確実にTrueとなる初期値を選択する。ただし例えばngの値を大きくしすぎると最大値が問題の閾値外になってしまうことがあるので注意。
    while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
        mid = (ok + ng) // 2
        # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
        if is_ok(a, mid):
            ok = mid
        else:
            ng = mid
    res = min(calc(a, ok), res)

print(res)