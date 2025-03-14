N, D = map(int, input().split())
s_list = [list(input()) for _ in range(N)]

res = 0
res_list = []
flag = False
for i in range(D):
    tmp = ""
    for j in range(N):
        tmp += s_list[j][i]

    if flag and tmp == "o" * N:
        res += 1
        res_list.append(res)
    elif not flag and tmp == "o" * N:
        res = 1
        res_list.append(res)
        flag = True
    else:
        flag = False

if len(res_list) > 0:
    print(max(res_list))
else:
    print(0)
