import math
import itertools as it
from collections import defaultdict


N, S, T = map(int, input().split())
input_lists = []
t_dict = defaultdict(int)
for i in range(N):
    A, B, C, D = map(int, input().split())
    input_lists.append([[A, B], [C, D]])
    t_dict[i] = math.sqrt(pow(abs(A-C), 2)+pow(abs(B-D), 2))/T

res = float("INF")
bit_lists = list(it.product([0, 1], repeat=2*N))
for p in it.permutations([i for i in range(N)]):
    for bit_list in bit_lists:
        tmp_res = 0
        pre_x, pre_y = 0, 0
        for i in range(len(p)):
            if bit_list[i*2:i*2+2].count(0) == 1:
                s_x, s_y = input_lists[p[i]][bit_list[i*2:i*2+2].index(0)]
                tmp_res += math.sqrt(pow(abs(s_x-pre_x), 2)+pow(abs(s_y-pre_y), 2))/S + t_dict[i]
                pre_x, pre_y = input_lists[p[i]][bit_list[i*2:i*2+2].index(1)]
            else:
                break
        else:
            res = min(tmp_res, res)

print(res)