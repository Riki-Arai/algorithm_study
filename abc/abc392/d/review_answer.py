from collections import defaultdict, Counter

N = int(input())

p2d_lists = [defaultdict(int) for _ in range(N)]
for i in range(N):
    a_list = list(map(int, input().split()))
    total = a_list[0]
    c_dict = Counter(a_list[1:])
    for k, v in c_dict.items():
        p2d_lists[i][k] = v/total

res = 0
for i in range(N):
    for j in range(i+1, N):
        tmp_res = 0
        p2d_dict = p2d_lists[i]
        p2d_dict2 = p2d_lists[j]
        for k, v in p2d_dict.items():
            if k in p2d_dict2:
                tmp_res += v*p2d_dict2[k]

        res = max(res, tmp_res)

print(res)