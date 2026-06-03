N = int(input())

A = [[list(map(int, input().split())) for _ in range(N)] for _ in range(N)]

S = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]