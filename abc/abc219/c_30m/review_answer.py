import sys, math, itertools as it, bisect as bi, functools as ft, copy, decimal, heapq as hq
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)


X = input().strip()
N = int(input())
S_list = [input() for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用

def comp(x, y):
    for xx, yy in zip(x, y):
        xx_i = X.index(xx)
        yy_i = X.index(yy)
        if xx_i > yy_i:
            return 1
        elif xx_i < yy_i:
            return -1

    if len(x) > len(y):
        return 1
    elif len(x) < len(y):
        return -1
    elif len(x) == len(y):
        return 0

S_list.sort(key=cmp_to_key(comp))
for s in S_list:
    print(s)





# 最初は愚直に解こうとしたが、結局cmp_to_keyを使用する方針に落ち着いた
# といってもcomp_to_keyを使用した方が良いとは最初から薄々考えてはいたが、慣れていないこともあり無意識に避けていた気がする
# なのでこの問題などを通してcomp_to_keyの理解を深めていきたい
import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

X = input().strip()
N = int(input())
S_list = [input() for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用

a_dict = {}
for i, x in enumerate(X, 1):
    a_dict[x] = i

def compare_to_key(arg1, arg2):
    for x, y in zip(arg1, arg2):
        if a_dict[x] > a_dict[y]: # よくみるとarg1(x)が大きい時はreturn 1となっている
            return 1
        elif a_dict[x] < a_dict[y]:
            return -1

    if len(arg1) > len(arg2): # 同様に文字列の大きさという基準においてarg1が大きいのでreturn 1
        return 1
    else:
        return -1

S_list.sort(key=functools.cmp_to_key(compare_to_key))
for s_list in S_list:
    print("".join(s_list))