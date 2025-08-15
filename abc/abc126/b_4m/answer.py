S = input().strip() # 取得例："A"

f_s = int(S[:2])
s_s = int(S[2:])

if 1 <= f_s <= 12 and 1 <= s_s <= 12:
    print("AMBIGUOUS")
elif 0 <= f_s <= 99 and 1 <= s_s <= 12:
    print("YYMM")
elif 1 <= f_s <= 12 and 0 <= s_s <= 99:
    print("MMYY")
else:
    print("NA")