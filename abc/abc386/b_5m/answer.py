S = input().strip()

zz_count = S.count("00")
rem_count = len(S) - zz_count * 2
print(zz_count + rem_count)