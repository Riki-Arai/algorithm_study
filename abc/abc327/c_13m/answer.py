A_lists = [input().split() for _ in range(9)]

n_set = set(i for i in range(1, 10))
for i in range(9):
    tmp_n_set = set()
    for j in range(9):
        tmp_n_set.add(int(A_lists[i][j]))
    if n_set != tmp_n_set:
        print("No")
        exit()

for j in range(9):
    tmp_n_set = set()
    for i in range(9):
        tmp_n_set.add(int(A_lists[i][j]))
    if n_set != tmp_n_set:
        print("No")
        exit()

for iw in range(3):
    for jw in range(3):
        cur_i = 3 * iw
        cur_j = 3 * jw
        tmp_n_set = set()
        for i in range(3):
            for j in range(3):
                tmp_n_set.add(int(A_lists[cur_i+i][cur_j+j]))

        if n_set != tmp_n_set:
            print("No")
            exit()

print("Yes")