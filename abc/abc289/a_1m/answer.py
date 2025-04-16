S_list = list(input())

res = ""
for s in S_list:
    if s == "0":
        res += "1"
    else:
        res += "0"

print(res)