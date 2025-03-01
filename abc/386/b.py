S = input()

count_1 = S.count("0")
count_2 = S.count("00")

S_exclude_zero = S.replace("0", "")
if count_1 == count_2 * 2:
    print(int((len(S_exclude_zero) + count_2)))

elif count_1 != count_2 * 2:
    one_zero_count = count_1 - count_2 * 2
    print(int((len(S_exclude_zero) + one_zero_count + count_2)))
