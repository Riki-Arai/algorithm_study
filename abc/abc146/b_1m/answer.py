N = int(input()) # 数値：1
S = input().strip() # 取得例："A"

alp_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
res = ""
for s in S:
    res += alp_list[(alp_list.index(s)+N)%26]

print(res)