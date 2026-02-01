import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, A, B = map(int, input().split())

sum_ = ((1+N)*N)//2
a_n = N//A
a_sum = (A+A*a_n)*a_n//2

b_n = N//B
b_sum = (B+B*b_n)*b_n//2

ab = math.lcm(A, B)
ab_n = N//ab
ab_sum = (ab+ab*ab_n)*ab_n//2

print(sum_-(a_sum+b_sum-ab_sum))