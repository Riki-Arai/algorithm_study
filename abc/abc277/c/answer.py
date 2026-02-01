import sys, math, itertools as it, bisect as bi, functools as ft, copy, decimal, heapq as hq
from collections import defaultdict, Counter, deque
sys.setrecursionlimit(10**7)

N = int(input())

g_dict = defaultdict(set)
for _ in range(N):
    A, B = map(int, input().split())
    g_dict[A].add(B)
    g_dict[B].add(A)

res = 1
seen_set = set()
def dfs(a):
    global res
    for b in g_dict[a]:
        if b not in seen_set:
            res = max(b, res)
            seen_set.add(b)
            dfs(b)

dfs(1)
print(res)