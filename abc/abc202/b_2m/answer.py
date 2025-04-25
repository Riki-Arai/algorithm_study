S = input().strip()

res = ""
res_dic = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
for s in S[::-1]:
    res += res_dic[s]

print(res)
