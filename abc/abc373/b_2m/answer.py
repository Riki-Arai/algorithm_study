S = input().strip()

res = 0
alp_list = [chr(i) for i in range(ord('B'), ord('Z') + 1)]
idx = S.index("A")
for a in alp_list:
    res += abs(idx - S.index(a))
    idx = S.index(a)
print(res)