Q = int(input()) # 数値：1

i = 0
res_list = []
for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        _, x = q[0], int(q[1])
        res_list.append(x)
    else:
        print(res_list[i])
        i += 1