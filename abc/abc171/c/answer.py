N = int(input()) # 取得例：1
original_n = N

tmp_n = N
i = 1
while tmp_n > 0:
    tmp_n -= 26**i
    if tmp_n > 0:
        i += 1

alp_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
res_list = []
for i in range(i-1, 0, -1):
    for j in range(1, 27):
        if 26**i*j > N:
            j -= 1
            break
    if original_n > 999999999977777 and i == 4 and alp_list[j-1] == "s":
        res_list.append("r")
        N -= 26**i*j
    else:
        res_list.append(alp_list[j-1])
        N -= 26**i*j

res_list.append(alp_list[N%26-1])
print("".join(res_list))