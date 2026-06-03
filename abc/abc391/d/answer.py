from collections import deque

N, W = map(int, input().split())

b_lists = [deque() for _ in range(W+1)]
Z_lists = []
for i in range(1, N+1):
    X, Y = map(int, input().split())
    Z_lists.append((Y, X, i))
