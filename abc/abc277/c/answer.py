import sys
from collections import defaultdict, deque, Counter
sys.setrecursionlimit(10**7)

N = int(input())

g_dict = defaultdict(list)
for _ in range(N):
    A, B = map(int, input().split())
    g_dict[A].append(B)
    g_dict[B].append(A)