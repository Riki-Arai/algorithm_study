# 正直どちらでもいいが、ソートのみをキーにした方が若干スマートであった
import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
S_list = [input() for _ in range(N)] # 取得例：["A","B"・・・"E"]、N行の入力用

res_dict = defaultdict(int)
for s in S_list:
    k = tuple(sorted(s))
    res_dict[k] += 1

res = 0
for s in S_list:
    k = tuple(sorted(s))
    if k in res_dict and res_dict[k] > 0:
        v = res_dict[k]
        v -= 1
        res += v
        res_dict[k] = v

print(res)

# first
#import sys, math, itertools, bisect, functools, copy, decimal
#from functools import cmp_to_key
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from sortedcontainers import SortedSet, SortedList, SortedDict
#from collections import defaultdict, Counter, deque
#from atcoder.dsu import DSU
#sys.setrecursionlimit(10**7)
#
#N = int(input()) # 数値：1
#S_list = [input() for _ in range(N)] # 取得例：["A","B"・・・"E"]、N行の入力用
#
#res_dict = defaultdict(int)
#for s in S_list:
#    c = Counter(s)
#    k = tuple(sorted(c.items()))
#    res_dict[k] += 1
#
#res = 0
#for s in S_list:
#    c = Counter(s)
#    k = tuple(sorted(c.items()))
#    if k in res_dict and res_dict[k] > 0:
#        v = res_dict[k]
#        v -= 1
#        res += v
#        res_dict[k] = v
#
#print(res)