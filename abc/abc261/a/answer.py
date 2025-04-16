L_1, R_1, L_2, R_2 = map(int, input().split())

res_list = [None] * 101
for i in range(L_1, R_1):
    res_list[i] = "R"

res = 0
for i in range(L_2, R_2):
    if res_list[i] == "R":
        res += 1

print(res)