from collections import defaultdict

N = int(input()) # 数値：1

sq_list = []
for x in range(1, 10**4+1):
    if x*x > 10**7:
        break
    sq_list.append(x*x)

res_dict = defaultdict(int)
for x in sq_list:
    for y in sq_list:
        if x < y and x + y <= N:
            res_dict[x+y] += 1

res_list = []
for k, v in res_dict.items():
    if v == 1:
        res_list.append(k)

print(len(res_list))
print(*sorted(res_list))