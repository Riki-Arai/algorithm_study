import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

N = int(input().strip())

g_dict = defaultdict(list)
for _ in range(N):
    s, t = input().split()
    g_dict[s].append(t)