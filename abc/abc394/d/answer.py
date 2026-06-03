from collections import defaultdict

S = input().strip()

res_dict = defaultdict(str)
res_dict["("] = ")"
res_dict["["] = "]"
res_dict["<"] = ">"
res_list = []
for s in S:
    if len(res_list) and res_list[-1] in res_dict and res_dict[res_list[-1]] == s:
        res_list.pop()
    else:
        res_list.append(s)

if len(res_list):
    print("No")
else:
    print("Yes")