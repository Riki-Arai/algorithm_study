from collections import defaultdict, deque, Counter

N = int(input()) # 数値：1
S_list = input().split()

res = 0
i = 0
max_i = max(map(len, S_list))
a2ss_dict = defaultdict(list)
alp_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for s in S_list:
    for k, a in enumerate(alp_list, 1):
        i2s_dict = defaultdict(str)
        if a == s[i]:
            i2s_dict[k] = a
            a2ss_dict[i2s_dict].append(s)
            break

k2v_lists = list(a2ss_dict.items())
for k, v in k2v_lists:
    if len(v) >= 2:
        res += len(v)*(len(v)-1)//2
    else:
        del a2ss_dict[k]

i += 1
while len(a2ss_dict) and i < max_i:
    kv_lists = list(a2ss_dict.items())
    a2ss_dict = defaultdict(list)
    for k, v in kv_lists:
        for s in v:
            for kk, a in enumerate(alp_list, 1):
                k[kk] = a
                if i < len(s) and s[i] == a:
                    a2ss_dict[k].append(s)

    k2v_lists = list(a2ss_dict.items())
    for k, v in k2v_lists:
        if len(v) >= 2:
            res += len(v)*(len(v)-1)//2
        else:
            del a2ss_dict[k]

    i += 1

print(res)