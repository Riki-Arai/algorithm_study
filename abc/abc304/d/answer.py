import bisect as bi
from collections import defaultdict

W, H = map(int, input().split())
N = int(input())

res_lists = []
for _ in range(N):
    p, q = map(int, input().split())
    res_lists.append((p, q))

A = int(input())
A_list = list(map(int, input().split()))
A_list.append(W)
A_list.sort()

B = int(input())
B_list = list(map(int, input().split()))
B_list.append(H)
B_list.sort()

res_dict = defaultdict(int)
for p, q in res_lists:
    w_b_i = bi.bisect_left(A_list, p)
    h_b_i = bi.bisect_left(B_list, q)
    res_dict[(w_b_i, h_b_i)] += 1

max_res = max(res_dict.values())
if len(res_dict) < (A + 1) * (B + 1):
    min_res = 0
else:
    min_res = min(res_dict.values())

print(min_res, max_res)