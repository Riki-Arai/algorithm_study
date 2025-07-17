# リスト内に答えが存在するわけではない点に注意し、二分探索を行う
# can_sell_buy内でリストの探索をしているが、探索回数が多くないので計算量はそこまで負担にはならない
# 今思うと買い手と売り手の数列をどうマージすれば良いかわからなかったことがACできなかった原因かも
# →マージした探索をしたい時もめぐる式を検討すると良いかも

def can_sell_buy(x, A, B):
    """
    条件を判定する関数:
    x円なら売ってもいい売り手の人数 >= x円で買ってもいい買い手の人数
    を満たすかどうかを True/False で返す。
    """
    na = sum(1 for a_i in A if a_i <= x)  # x円以下で売れる売り手
    nb = sum(1 for b_i in B if b_i >= x)  # x円以上で買える買い手
    return na >= nb

N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

low, high = 0, 10**9+1
while high - low > 1:
    mid = (low + high) // 2
    if can_sell_buy(mid, A_list, B_list):
        high = mid
    else:
        low = mid

print(high)


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