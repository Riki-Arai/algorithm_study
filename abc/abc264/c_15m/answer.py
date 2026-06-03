import itertools as it

H, W = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(H)]

H_1, W_2 = map(int, input().split())
B_lists = [list(map(int, input().split())) for _ in range(H_1)]

row_bit_lists = list(it.product([0, 1], repeat=H))
col_bit_lists = list(it.product([0, 1], repeat=W))