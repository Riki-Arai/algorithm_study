S = int(input()) # 取得例：1

for n in S:
    res += int(n)

if res % 9 == 0:
    print("Yes")
else:
    print("No")