import collections

S_list = list(input())
c_count = collections.Counter(S_list)
res_dic = collections.defaultdict(list)
for k, v in c_count.items():
    res_dic[v].append(k)

for v in res_dic.values():
    if len(v) != 2:
        print("No")
        exit()

print("Yes")