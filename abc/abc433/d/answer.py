N, M = map(int, input().split()) # 取得例：1 2

res = 0
b_sets = set()
for _ in range(M):
    R, C = map(int, input().split()) # 取得例：1 2
    add_flag = True
    for i in [0, 1]:
        for j in [0, 1]:
            if (R+i, C+j) in b_sets:
                add_flag = False
                break

    if add_flag:
        res += 1
        for i in [0, 1]:
            for j in [0, 1]:
                b_sets.add((R+i, C+j))

print(res)