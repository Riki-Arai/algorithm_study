S = input().strip()

res_list = []
for i in range(1, len(S)+1):
    tmp_s = S[i:] + S[:i]
    res_list.append(tmp_s)

res_list.sort()
print(res_list[0])
print(res_list[-1])