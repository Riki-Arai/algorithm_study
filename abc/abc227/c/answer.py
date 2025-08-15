import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input())

def max_A_le_B(n):
    rootN = math.isqrt(n)
    for a in range(rootN, 0, -1):
        # ここで n を使う
        if n % a == 0:
            return a
    return None

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

res = 0
max_b = max_A_le_B(N)
max_a = max_A_le_B(max_b)
for b in range(1, max_b):
    make_divisors(b)
        #if a <= b:
        #    c = N//(b)
        #    if b <= c:
        #        max_a = max_A_le_B(b)
        #        if max_a == 1:
        #            res += max_a*((c-b)+1)
        #        else:
        #            res += ((c-b)+1) + ((c-b//max_a)+1)