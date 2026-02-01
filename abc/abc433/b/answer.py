N = int(input()) # 数値：1

g_lists = [[""]*N for _ in range(N)]
i = 0
j = (N-1)//2
n = 1
g_lists[i][j] = str(n)
for _ in range(N**2-1):
    tmp_i = (i-1)%N
    tmp_j = (j+1)%N
    n += 1
    if g_lists[tmp_i][tmp_j] == "":
        g_lists[tmp_i][tmp_j] = str(n)
        i = tmp_i
        j = tmp_j
    else:
        i = (i+1)%N
        g_lists[i][j] = str(n)

for g_list in g_lists:
    print(*g_list)