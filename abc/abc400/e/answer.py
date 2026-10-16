import sys; sys.setrecursionlimit(10**7)

Q = int(input()) # 数値：1

# 計算量はO(NloglogN)
def sieve_of_eratosthenes(n: int) -> list[int]:
    """n以下の素数を高速に列挙する (エラトステネスの篩)"""
    if n < 2:
        return []
    
    size = (n - 1) // 2 + 1
    is_prime = [True] * size
    is_prime[0] = False
    
    for i in range(1, int(n**0.5) // 2 + 1):
        if is_prime[i]:
            p = 2 * i + 1
            start = (p * p) // 2
            is_prime[start::p] = [False] * ((size - start - 1) // p + 1)
            
    return [2] + [2 * i + 1 for i, prime in enumerate(is_prime) if prime]

p_list = sieve_of_eratosthenes(10**6)

for _ in range(Q):
    A = int(input()) # 数値：1