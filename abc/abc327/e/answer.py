'''
(1) bit全探索をすれば解答ができるがTLEになるのでDPを適用したい
(2) しかし選ぶものが増えるほど、事前に選んだスコアに対する重みがしてしまうので計算をし直さないといけない
(3) そこで後ろから計算をすることで左へずらすごとに重みに0.9ずつかけていけば済むのでDPを適用できる
(4) この問題では後ろから考えることで前の影響をなくすことができたが、実装が少し複雑になってしまっており、公式の方法を学んだ方がいい
    →実際には前からでもDPを適用することは可能
(5) 今回は分子といったように影響のある部分に着目して解くことが重要
'''

from math import sqrt

N = int(input()) # 数値：1
P = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
INF = float("inf")
dp = [-INF] * (N + 1)
dp[0] = 0
for i in range(N):
    for k in range(i, -1, -1):
        dp[k + 1] = max(dp[k + 1], 0.9 * dp[k] + P[i])

ans = -INF
denom = 0
for k in range(1, N + 1):
    denom = 0.9 * denom + 1
    ans = max(ans, dp[k] / denom - 1200 / sqrt(k))
print(ans)


### 自分の解答(C++に変換してAC)
#import sys; sys.setrecursionlimit(10**7)
#
#N = int(input()) # 数値：1
#P_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
#
#P_list.reverse()
#dp_lists = [[[-float("INF"), -float("INF"), -float("INF")]]*N for _ in range(N)]
#dp_lists[0][0] = [P_list[0], 1, P_list[0]-1200]
#for i in range(1, N):
#    for j in range(N-2 , -1, -1):
#        if dp_lists[i-1][j][2] != -float("INF"):
#            d, m, r = dp_lists[i-1][j]
#            dd = d+P_list[i]*0.9**(j+1)
#            mm = (m+0.9**(j+1))
#            rr = dd/mm - (1200/(pow(j+2, 1/2)))
#            if rr > dp_lists[i][j+1][2]:
#                dp_lists[i][j+1] = [dd, mm, rr]
#
#            if dp_lists[i-1][j][2] > dp_lists[i][j][2]:
#                dp_lists[i][j] = dp_lists[i-1][j]
#
#        if j == 0 and P_list[i]-1200 > dp_lists[i-1][j][2]:
#            dp_lists[i][j] = [P_list[i], 1, P_list[i]-1200] 
#
#res = -float("INF")
#for i in range(N):
#    for j in range(N):
#        res = max(dp_lists[i][j][2], res)
#
#print(res)