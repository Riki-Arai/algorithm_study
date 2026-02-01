from collections import Counter

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


def prime_factorize(n):
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    divisor = pollard_rho(n)
    return prime_factorize(divisor) + prime_factorize(n // divisor)

T = int(input())
for _ in range(T):
    N = int(input())
    factors = prime_factorize(N)

    cnt = Counter(factors)
    p, q = None, None
    for prime, c in cnt.items():
        if c == 2:
            p = prime
        else:
            q = prime

    print(p, q)