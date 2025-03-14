s_list = [input() for _ in range(8)]
s_list.reverse()

alp_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
row_res = 1
for s in s_list:
    if "*"  in s:
        alp_res = alp_list[s.find("*")]
        print(alp_res + str(row_res))
        exit()
    row_res += 1
