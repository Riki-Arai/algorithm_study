N = int(input())
S = input()

r = g = b = 0

for c in S:
    if c == 'R':
        r += 1
    elif c == 'G':
        g += 1
    else:
        b += 1

all_count = r * g * b
sub = 0

for i in range(N):
    for j in range(i + 1, N):
        if S[i] == S[j]:
            continue
        k = 2 * j - i
        if k >= N:
            continue
        if S[k] == S[i] or S[k] == S[j]:
            continue
        sub += 1

print(all_count - sub)


import bisect as bi
from collections import defaultdict

N = int(input().strip())
S = input().strip() # 取得例：A

s2i_dicts = defaultdict(list)
for i, s in enumerate(S):
    s2i_dicts[s].append(i)

def f(a_list, b_list, c_list, res):
    for i in a_list:
        for j in b_list:
            if i < j:
                b_i = bi.bisect_left(c_list, j+(j-i))
                if b_i < len(c_list):
                    if c_list[b_i]-j != j-i:
                        b_ii = bi.bisect_left(c_list, j)
                        if b_ii < len(c_list):
                            res += len(c_list)-b_ii
                    elif c_list[b_i]-j == j-i:
                        b_ii = bi.bisect_left(c_list, j)
                        if b_ii < len(c_list):
                            res += len(c_list)-(b_ii+1)
                else:
                    b_ii = bi.bisect_left(c_list, j)
                    if b_ii < len(c_list):
                        res += len(c_list)-b_ii

    return res

i_lists = list(s2i_dicts.values())
if len(i_lists) == 3:
    res = 0
    res += f(i_lists[1], i_lists[2], i_lists[0], 0)
    res += f(i_lists[2], i_lists[1], i_lists[0], 0)
    res += f(i_lists[0], i_lists[2], i_lists[1], 0)
    res += f(i_lists[2], i_lists[0], i_lists[1], 0)
    res += f(i_lists[0], i_lists[1], i_lists[2], 0)
    res += f(i_lists[1], i_lists[0], i_lists[2], 0)
    print(res)
else:
    print(0)