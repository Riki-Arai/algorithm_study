S = input().strip() # 取得例："A"

for i, s in enumerate(S, 1):
    if not(i%2 == 0 and s in ("L", "U", "D")) and not(i%2 != 0 and s in ("R", "U", "D")):
        print("No")
        exit()

print("Yes")