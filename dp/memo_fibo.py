import sys
sys.setrecursionlimit(10**7)

N = int(input().strip())

memo_dict = dict()
def f(n):
    if n in memo_dict:
        return memo_dict[n]
    if n == 1:
        return 1
    elif n == 2:
        return 1

    res = f(n-2)%1000000007+f(n-1)%1000000007
    memo_dict[n] = res
    return res

print(f(N))
