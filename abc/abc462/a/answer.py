S = input().strip() # 取得例："A"

alp_set = set([chr(i) for i in range(ord('a'), ord('z') + 1)])
res_list = []
for s in S:
    if s not in alp_set:
        res_list.append(s)

print("".join(res_list))