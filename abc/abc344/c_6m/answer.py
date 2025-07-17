A_lists = [list(map(int, input().split())) for _ in range(8)]

A_list = A_lists[1]
B_list = A_lists[3]
C_list = A_lists[5]
X_list = A_lists[7]

res_set = set()
for a in A_list:
    for b in B_list:
        for c in C_list:
            res_set.add(a+b+c)

for x in X_list:
    if x in res_set:
        print("Yes")
    else:
        print("No")