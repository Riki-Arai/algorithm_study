S = input().strip() # 取得例："A"

s_list = S.split("-")
i, j = int(s_list[0]), int(s_list[1])
if j == 8:
    print(f"{i+1}-{1}")
else:
    print(f"{i}-{j+1}")