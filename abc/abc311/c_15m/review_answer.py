# 解説ではFunctional GraphのN回移動することでサイクルに到達する性質を利用して解いている
# 有向グラフなどは辞書を使えば良いことがわかってはきたが、楽な実装方法があれば覚えておきたいところ

N = int(input())
A = list(map(int, ("0 " + input()).split()))
now = 1
for _ in range(N):
    now = A[now]# 予めN回移動する

B = [now]
while B[0] != A[now]:
	now = A[now]
	B.append(now)
print(len(B))
print(*B)


#import math, itertools, bisect, functools, copy, decimal
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from collections import defaultdict, Counter, deque
#
#N = int(input())
#A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#res_dict = {}
#for i, a in enumerate(A_list, 1):
#    res_dict[i] = a
#
#for i in range(1, N+1):
#    ii = i
#    res_set = set()
#    res_list = []
#    while True:
#        res_set.add(ii)
#        res_list.append(ii)
#        next_edge = res_dict[ii]
#        if next_edge in res_set:
#            final_res_list = []
#            idx = res_list.index(next_edge)
#            for j in range(idx, len(res_list)):
#                final_res_list.append(res_list[j])
#            print(len(final_res_list))
#            print(*final_res_list)
#            exit()
#        ii = next_edge