S = input().strip() # 取得例："A"

res_list = []
for s in S:
    if s.isupper():
        res_list.append(s)

print("".join(res_list))