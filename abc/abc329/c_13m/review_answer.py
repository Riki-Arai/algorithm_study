# 文字列や数列で蓮ぞかどうかに関する問題はランレングス圧縮を検討すると良さそう
import math, itertools, bisect, functools, copy, decimal
import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

N = int(input())
S = input().strip()

alp_dict = {chr(i):0 for i in range(ord('a'), ord('z') + 1)}
for k, v in itertools.groupby(list(S)):
    alp_dict[k] = max(alp_dict[k], len(list(v)))

print(sum(list(alp_dict.values())))

## first
#N = int(input())
#S = input().strip()
#
#alp_dict = {chr(i):0 for i in range(ord('a'), ord('z') + 1)}
#alp_dict[S[0]] = 1
#count = 1
#for i in range(1, N):
#    if S[i-1] == S[i]:
#        count += 1
#        if count > alp_dict[S[i]]:
#            alp_dict[S[i]] = count
#    else:
#        if alp_dict[S[i]] == 0:
#            alp_dict[S[i]] = 1
#        count = 1
#
#print(sum(list(alp_dict.values())))