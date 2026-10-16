from collections import deque

H, W = map(int, input().split())
S_lists = [list(input()) for _ in range(H)]
A, B, C, D = map(int, input().split())

A -= 1
B -= 1
C -= 1
D -= 1
move_lists = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}.values()