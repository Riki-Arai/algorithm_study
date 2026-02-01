from collections import defaultdict

N, K = map(int, input().split())
A_list = list(map(int, input().split()))

cum_list = [0]
for a in A_list:
    cum_list.append(cum_list[-1]+a)

res = 0
res_dict = defaultdict(int)
for r in range(1, len(cum_list)):
    res_dict[cum_list[r-1]] += 1
    res += res_dict[cum_list[r]-K]

print(res)