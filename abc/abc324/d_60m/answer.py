import itertools as it, bisect as bi
from collections import defaultdict, Counter

N = int(input())
S = input().strip()

n_set = set()
for i in range(10**7):
    ii = i**2
    if len(str(ii)) > 13:
        break
    n_set.add(str(ii))

s_dict = defaultdict(int)
for s in sorted(list(S)):
    s_dict[s] += 1

res = 0
for n in n_set:
    n_dict = Counter(n)
    for k, v in s_dict.items():
        if k == "0":
            if "0" in n_dict and n_dict["0"] > v:
                break
        else:
            if k not in n_dict:
                break
            elif n_dict[k] != v:
                break
    else:
        for k in n_dict.keys():
            if k not in s_dict:
                break
        else:
            res += 1

print(res)