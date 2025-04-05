N, M = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

if M == 0:
    print(*[i for i in range(1, N+1)])
else:
    tmp_list = [i for i in range(1, N)]
    idx = 0
    for a in A_list:
        tmp_list.insert(a+idx, "*")
        idx += 1
    if tmp_list[-1] == "*":
        tmp_list.append(tmp_list[-2]+1)

    tmp2_list = []
    res_list = []
    for j in range(len(tmp_list)-1):
        if tmp_list[j] != "#" and tmp_list[j+1] == "#":
            tmp2_list.append(tmp_list[j])
        elif len(tmp2_list) > 0 and not (tmp_list[j] != "#" and tmp_list[j+1] == "#"):
            for k in range(j, tmp2_list[0]-1, -1):
                res_list.append(k)
        else:
            res_list.append(tmp_list[j])

print(*res_list)
