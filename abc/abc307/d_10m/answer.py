N = int(input())
S = input().strip()

res_list = [""]
for s in S:
    if s == "(":
        res_list.append(s)
    elif s == ")" and len(res_list[-1]) and res_list[-1][0] == "(":
        res_list.pop()
    else:
        res_list[-1] += s

print("".join(res_list))