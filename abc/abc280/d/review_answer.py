import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU

sys.setrecursionlimit(10**7)

# ---- 与えられているコードここから ----
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
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    import random
    if n % 2 == 0:
        return 2
    if is_prime(n):
        return n
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

def prime_factorize(n):
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    divisor = pollard_rho(n)
    return prime_factorize(divisor) + prime_factorize(n // divisor)

# ルジャンドルの定理
def legendre_formula(N, p):
    count = 0
    power = p
    while power <= N:
        count += N // power
        power *= p
    return count

def min_N_for_prime_power(p, e):
    """
    「N! に含まれる p の指数 >= e」となる最小の N を
    二分探索で求める
    """
    left, right = 1, 2 * 10**12  # 十分大きい上限を取る
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if legendre_formula(mid, p) >= e:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

K = int(sys.stdin.readline().strip())
p_list = prime_factorize(K)
# それぞれの素因数を指数としてカウント
cnt = Counter(p_list)
# 各prime^exponent(指数)について、必要となる最大のNを求める
res = 0
for prime, exponent in cnt.items():
    # それぞれの素数でp^eを含む最低のN!(≒N)を求め、そのうちの最大を選択すれば全てのp^eを含むといえる
    res = max(res, min_N_for_prime_power(prime, exponent))

print(res)