import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

N = int(input())

res_dict = defaultdict(int)
def f(n):
    if n <= 1:
        return 0
    if n not in res_dict:
        res_dict[n] = n + f(n//2) + f((n+1)//2)

    return res_dict[n]

print(f(N))