M, D = map(int, input().split())
res = 0
for m in range(1, M+1):
    for d in range(1, D+1):
        str_d = str(d)
        if len(str_d) == 2:
            d_1 = int(str_d[0])
            d_2 = int(str_d[1])
            if d_1 >= 2 and d_2 >= 2 and m == d_1 * d_2:
                res += 1
print(res)