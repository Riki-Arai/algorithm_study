import sys, math, itertools as it, bisect as bi, functools as ft, copy, decimal, heapq as hq
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

def miller_rabin(n):
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for sp in small_primes:
        if n == sp:
            return True
        if n % sp == 0 and n != sp:
            return False

    test_bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False

    for a in test_bases:
        if a % n == 0:  # a が n と同じ場合はスキップ
            return True
        if not check(a, s, d, n):
            return False
    return True


def is_prime(n):
    return miller_rabin(n)


def gcd(a, b):
    """ユークリッドの互除法"""
    while b:
        a, b = b, a % b
    return a


def pollard_rho(n):
    import random

    if n % 2 == 0:
        return 2
    if is_prime(n):
        return n  # n が素数の場合はそのまま返す

    while True:
        x = random.randrange(2, n - 1)
        c = random.randrange(1, n - 1)
        y = x
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = gcd(abs(x - y), n)
            if d == n:
                break
        if d > 1 and d < n:
            return d


###### 注意! 取得したリストの中身はランダムなので必要によっては常に同じ結果が欲しい時はsortをすること
def prime_factorize(n):
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    divisor = pollard_rho(n)
    return prime_factorize(divisor) + prime_factorize(n // divisor)


T = int(input()) # 数値：1

for _ in range(T):
    N = int(input()) # 数値：1
    A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
    res_dict = defaultdict(SortedList)
    res2_dict = defaultdict(dict)
    res3_dict = defaultdict(set)
    for a in A_list:
        p_dict = Counter(prime_factorize(a))
        res2_dict[a] = p_dict
        for k, v in p_dict.items():
            if v not in res3_dict[k]:
                res_dict[k].add(v)
                res3_dict[k].add(v)

    lcm = math.lcm(*A_list)
    lcm_dict = Counter(prime_factorize(lcm))
    res_list = []
    for a in A_list:
        res = lcm
        p_dict = res2_dict[a]
        for k, v in p_dict.items():
            if k in lcm_dict and lcm_dict[k] == v:
                if len(res_dict[k]) >= 2:
                    res = (res // k**(v-res_dict[k][-2])) % 998244353
                else:
                    res = (res // k**v) % 998244353

        res_list.append(res%998244353)

    print(*res_list)