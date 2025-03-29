S = input().strip()
T = input().strip()

s_idx = 0
res_list = []
for i in range(len(T)):
    if S[s_idx] == T[i]:
        res_list.append(i+1)
        s_idx += 1

print(*res_list)