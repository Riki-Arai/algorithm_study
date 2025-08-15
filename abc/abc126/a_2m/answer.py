N, K = map(int, input().split()) # 取得例：1 2
S = input().strip() # 取得例："A"

res_list = []
for i in range(len(S)):
    if i == K-1:
        res_list.append(S[i].lower())
    else:
        res_list.append(S[i])

print("".join(res_list))
