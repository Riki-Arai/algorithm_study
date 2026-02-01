from collections import defaultdict

N = int(input())

memo_dict = defaultdict(int)
def f(k):
    if k == 0:
        return 1
    if k not in memo_dict:
        memo_dict[k] = f(k//2)+f(k//3)

    return memo_dict[k]

print(f(N))