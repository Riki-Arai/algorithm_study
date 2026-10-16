from collections import defaultdict

N = int(input()) # 数値：1

input_lists = []
n2c_dict = defaultdict(int)
for _ in range(N):
    A, B, C = map(int, input().split()) # 取得例：1 2
    input_lists.append((C, A, B))
    n2c_dict[A] += 1
    n2c_dict[B] += 1

if sorted(list(n2c_dict.values()))[-1] >= 