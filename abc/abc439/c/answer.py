N = int(input().strip())

tmp_res_list = [0]*(N+1)
for x in range(1, 10**4+1):
    xx = x**2
    for y in range(x+1, 10**4+1):
        yy = y**2
        if xx + yy > N:
            break
        tmp_res_list[xx+yy] += 1

res_list = []
for i, x in enumerate(tmp_res_list):
    if x == 1:
        res_list.append(i)

print(len(res_list))
print(*res_list)