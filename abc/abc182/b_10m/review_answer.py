N = int(input())
A = list(map(int, input().split()))

ans = -1
mx = 0
for x in range(2, 1001):
    s = sum(a % x == 0 for a in A)
    if mx < s:
        mx = s
        ans = x

print(ans)


## first
#import math, itertools, bisect, functools, copy
#from collections import defaultdict, Counter, deque
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て
#
#N = int(input()) # 取得例：1
#A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
#
#res = 0
#res_dic = defaultdict(list)
#for i in range(2, 1001):
#    tmp_res = 0
#    for a in A_list:
#        if a % i == 0:
#            tmp_res += 1
#    res = max(res, tmp_res)
#    res_dic[tmp_res].append(i)
#
#print(res_dic[res][0])