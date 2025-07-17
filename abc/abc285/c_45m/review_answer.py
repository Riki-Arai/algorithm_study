S = input().strip()

res = 0
alp_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
r_s = S[::-1]
for i in range(len(r_s)):
    res += 26**i * (alp_list.index(r_s[i])+1)

print(res)