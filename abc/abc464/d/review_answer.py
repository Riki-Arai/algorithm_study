import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, product
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    X = list(map(int, input().split()))        
    Y = list(map(int, input().split()))

    dp = [[-float("INF"), -float("INF")] for _ in range(N)]
    if S[0] == 'S':
        dp[0] = [0, -X[0]]
    else:
        dp[0] = [-X[0], 0]

    for i in range(N-1):
        if S[i+1] == 'S':
            dp[i+1][0] = max(dp[i][0], dp[i][1] + Y[i])
            dp[i+1][1] = max(dp[i][0] - X[i+1], dp[i][1] - X[i+1])
        else:
            dp[i+1][0] = max(dp[i][0] - X[i+1], dp[i][1] - X[i+1] + Y[i])
            dp[i+1][1] = max(dp[i][0], dp[i][1])

    print(max(dp[N-1]))