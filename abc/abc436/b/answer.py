N = input().strip() # 取得例："A"

for _ in range(10**7):
    res = 0
    for i in list(N):
        res += int(i)*int(i)
    if res == 1:
        print("Yes")
        exit()
    N = str(res)

print("No")