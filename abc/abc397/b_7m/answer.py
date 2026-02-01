S = input().strip() # 取得例："A"

res = 0
for i, s in enumerate(list(S), 1):
    if (i+res) % 2 == 1 and s != "i":
        res += 1
    elif (i+res) % 2 == 0 and s != "o":
        res += 1

if (len(S)+res) % 2 == 0:
    print(res)
else:
    print(res+1)