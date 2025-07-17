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