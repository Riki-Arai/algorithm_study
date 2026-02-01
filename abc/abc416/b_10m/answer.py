S = input().strip() # 取得例："A"

T_list = [""] * len(S)
res_flag = False
for i in range(len(S)):
    s = S[i]
    if s == "." and not res_flag:
        T_list[i] = "o"
        res_flag = True
    elif s == "#":
        T_list[i] = "#"
        res_flag = False
    else:
        T_list[i] = "."

print("".join(T_list))