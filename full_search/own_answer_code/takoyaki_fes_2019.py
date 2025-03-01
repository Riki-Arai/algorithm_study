import itertools

N = int(input())
D = list(map(int, input().split()))

d_comb = itertools.combinations(D, 2)
re_list = []
for c in d_comb:
    re_list.append(c[0] * c[1])

print(sum(re_list))
