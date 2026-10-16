'''
※解説AC
(1) 当初は貪欲法で解こうとしたがどの戦略でも判例が出てしまってACできず（方法自体はあるらしい）
(2) しかし2変数で最大値を求めたい問題という構図なので二分探索を候補に入れるべきだった
(3) 今回のケースではドリンクの融通が効かないのでまずはドリンクの購入数を決め内し、デザートは残りのお金で全て買うのでそちらを二分探索で求めていくと良かった
(4) 今回の敗因は貪欲法の証明をよく理解していないこと、二分探索を候補から外していた点にある
(5) ある制約においての最大や最小を求めるのであれば、2変数のうちの1つを固定して二分探索をする形式を検討すると良さそう
'''
import bisect as bi

N, M, K = map(int, input().split()) # 取得例：1 2
X, Y = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

A_list.sort()
B_list.sort()
cum_list = [0]
for a in A_list:
    cum_list.append(cum_list[-1]+a)

sum_ = X+K*Y
res = bi.bisect_right(cum_list, sum_)-1
for i, b in enumerate(B_list, 1):
    if Y-(b+K-1)//K >= 0:
        Y -= (b+K-1)//K
        sum_ -= b
        res = max(i+bi.bisect_right(cum_list, sum_)-1, res)
    else:
        break

print(res)