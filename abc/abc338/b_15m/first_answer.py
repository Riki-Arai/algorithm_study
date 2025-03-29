import collections

S_list = list(input())

s_counter = collections.Counter(S_list)
res_dic = {}
max_v = 0
for x in s_counter:
    max_v = max(max_v, s_counter[x])
    if s_counter[x] in res_dic:
        tmp_list = res_dic[s_counter[x]]        
        tmp_list.append(x)
        res_dic[s_counter[x]] = tmp_list 
    else:
        res_dic[s_counter[x]] = [x]

res_list = res_dic[max_v]
alp_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for a in alp_list:
    if a in res_list:
        print(a)
        exit()