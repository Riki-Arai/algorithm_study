p, q = input().split()

tmp_list = [p, q]
tmp_list.sort()
f_idx = tmp_list[0]
s_idx = tmp_list[1]
idx_dic = {"A": 0, "B": 3, "C": 4, "D": 8, "E": 9, "F": 14, "G": 23}
print(idx_dic[s_idx]-idx_dic[f_idx])