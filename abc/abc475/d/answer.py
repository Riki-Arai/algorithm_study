'''
(1) 素数判定や列挙は実は数が多くないので、素数に関する問題が来たときは愚直な手法でも間に合ったりする
(2) Sと素数が同じ型をしているかどうかは気合いで書く
'''
from collections import defaultdict

S = input().strip() # 取得例："A"

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

s2is_dict = defaultdict(list)
for i, s in enumerate(S):
    s2is_dict[s].append(i)

p_list = sieve_of_eratosthenes(10**len(S))
for p in p_list:
    p = str(p)
    if len(p) == len(S):
        for i_list in s2is_dict.values():
            tmp_set = set()
            for i in i_list:
                tmp_set.add(p[i])
            if len(tmp_set) > 1:
                break
        else:
            if len(set(p)) == len(set(S)):
                print(p)
                exit()

print(-1)