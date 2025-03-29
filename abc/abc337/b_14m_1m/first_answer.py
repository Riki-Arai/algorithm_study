S = input().strip()

a_list = ["A", "B", "C"]
res_list = []
for s in S:
    res_list.append(a_list.index(s))

sorted_res_list = sorted(res_list)
if res_list == sorted_res_list:
    print("Yes")
else:
    print("No")