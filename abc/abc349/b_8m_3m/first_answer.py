import collections

S_list = list(input())

c_list = collections.Counter(S_list)
res_list = []
for k in c_list:
    res_list.append(c_list[k])

c_list = collections.Counter(res_list) 
for k in c_list:
    v = c_list[k]
    if v != 2 and v != 0:
        print("No")
        exit()

print("Yes")