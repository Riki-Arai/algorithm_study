from collections import defaultdict

N = int(input())

A_lists = []
for _ in range(N):
    C = int(input())
    A_lists.append(list(map(int, input().split())))

X = int(input())
