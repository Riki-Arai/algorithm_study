N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)]

A_lists.sort(key=lambda x: x[0])
res_lists = []
for l, r in A_lists:
    if not len(res_lists) or res_lists[-1][1] < l:
        res_lists.append([l, r])
    else:
        res_lists[-1][1] = max(res_lists[-1][1], r)

for res_list in res_lists:
    print(*res_list)