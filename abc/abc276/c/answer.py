N = int(input().strip())
P_list = list(map(int, input().split()))

idx_n = dict()
P_list = P_list[::-1]
for i in range(N-1):
    idx_n[i] = P_list[i]
    if P_list[i] <= P_list[i+1]:
        tmp_p_list = P_list[:i+1].copy()
        next_n = P_list[i+1]
        tmp_p_list.remove(next_n-1)
        tmp_p_list.append(next_n)
        tmp_p_list.sort(reverse=True)
        if i+2 < N -1:
            res_list = P_list[i+2:][::-1]
        else:
            res_list = P_list[i+1:][::-1]
        res_list.append(next_n-1)
        print(*res_list + tmp_p_list)
        exit()