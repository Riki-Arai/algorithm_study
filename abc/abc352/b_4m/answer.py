S = input().strip()
T = input().strip()

i = 0
res_list = []
while i < len(S):
    for j, s in enumerate(list(T), 1):
        if S[i] == s:
            res_list.append(j)
            i += 1

print(*res_list)