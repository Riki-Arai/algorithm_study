# 二分探索版
import math
import bisect


N = int(input())

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

p_list = []
for x in range(1, 10**6+1):
    if is_prime(x):
        p_list.append(x)

res = 0
for i in range(len(p_list)):
    a = p_list[i]
    if a**5 > N:
        break
    for j in range(i+1, len(p_list)):
        b = p_list[j]
        if (a**2)*(b**3) > N:
            break
        c = math.isqrt(N//(a**2*b))
        b_i = bisect.bisect_left(p_list, c)
        if is_prime(c):
            res += b_i-j
        else:
            res += b_i-j-1

print(res)


# 累積和
import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input())

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

prime_set = set()
# 素数の個数の累積和をカウント
pn_cum_list = [0] * (10**6+1)
for n in range(1, 10**6+1):
    if is_prime(n):
        prime_set.add(n)
        pn_cum_list[n] = pn_cum_list[n-1] + 1
    else:
        pn_cum_list[n] = pn_cum_list[n-1]

res = 0
for a in prime_set:
    if a**5 > N:
        break
    for b in prime_set:
        if b**3 > N:
            break
        if b > a:
            # isqrtを利用して切り捨てをするイメージ
            c = int(math.isqrt(N // (a*a*b)))
            if b < c:
                res += pn_cum_list[c] - pn_cum_list[b]

print(res)