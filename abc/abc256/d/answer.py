N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)]

A_lists.sort()
res_lists = [[A_lists[0][0], A_lists[0][1]]]
for x, y in A_lists[1:]:
    if x <= res_lists[-1][1]:
        res_lists[-1][1] = max(res_lists[-1][1], y)
    else:
        res_lists.append([x, y])

for x, y in res_lists:
    print(x, y)