S = input().strip()

res = 0
for i in range(10**4):
    res_list = [False] * 10
    for _ in range(4):
        m, r = divmod(i, 10)
        res_list[r] = True
        i = m

    for j, s in enumerate(S):
        if s == "o" and res_list[j] == False:
            break
        if s == "x" and res_list[j] == True:
            break

    else:
        res += 1

print(res)