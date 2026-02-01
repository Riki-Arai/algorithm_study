# 二分探索自体は9回しかないので、is_okの全探索を2回行っても十分に間に合う
# nが低い時は常にFalseであるが、途中からは売りたい人が増えて買いたい人は減るので単調性が成立することから、二分探索が使える（昔はこれが理解できていなかった）
N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

def is_ok(n):
    sale_num = 0
    for a in A_list:
        if n >= a:
            sale_num += 1
    buy_num = 0
    for b in B_list:
        if n <= b:
            buy_num += 1
    if sale_num >= buy_num:
        return True
    else:
        return False

ok, ng = 10**9+1, 0  # 最大値を導出する場合は左側で確実にTrueとなる初期値を選択する。ただし例えばngの値を大きくしすぎると最大値が問題の閾値外になってしまうことがあるので注意。
while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
    mid = (ok + ng) // 2
    # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)


# first（WAなので注意）
#import math, itertools, bisect, functools, copy, decimal
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from collections import defaultdict, Counter, deque
#
#N, M = map(int, input().split())
#A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#sale_p = 0
#A_list.sort()
#B_list.sort()
#r_b_list = sorted(list(map(lambda x: -x, B_list)))
#for i, a in enumerate(A_list, 1):
#    num = M - bisect.bisect_right(r_b_list, -a)
#    if i >= num:
#        sale_p = max(a, sale_p)
#
#buy_p = float("INF")
#for i, b in enumerate(B_list, 1):
#    num = bisect.bisect_left(A_list, b)
#    if num >= M - i and num - 1 >= 0:
#        buy_p = min(A_list[num-1], buy_p)
#
#if buy_p == float("INF"):
#    print(max(B_list)+1)
#else:
#    print(min(buy_p, sale_p))