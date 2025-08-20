N = int(input().strip())
P_list = list(map(int, input().split()))

#tmp_idx = 0
for i in range(N-1, 0, -1):
    if P_list[i] < P_list[i-1]:
        tmp_idx = i-1
        break

c_p_list = P_list[tmp_idx:].copy()
tmp_num = P_list[tmp_idx]-1
c_p_list.remove(tmp_num)
print(*P_list[:tmp_idx] + [tmp_num] + sorted(c_p_list, reverse=True))