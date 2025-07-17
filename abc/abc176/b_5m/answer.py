S = input().strip() # 取得例：1

res = 0
for s in S:
    res += int(s)

if res % 9 == 0:
    print("Yes")
else:
    print("No")