N = int(input())

res_lists = []
for i in range(N):
    res_list = []
    for j in range(i+1):
        if j == 0 or i == j:
            res_list.append(1)
        else:
            res_list.append(res_lists[i-1][j-1]+res_lists[i-1][j])

    res_lists.append(res_list)

for res_list in res_lists:
    print(*res_list)