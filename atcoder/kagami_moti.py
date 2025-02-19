import sys

N = int(input())
D = [int(input()) for _ in range(N)]

D.sort(reverse=True)
print(len(set(D)))
