S = input().strip() # 取得例："A"

res = 0
for i in range(len(S)):
    count = 0
    if S[i] == "t":
        count += 1
        for j in range(i+1, len(S)):
            if S[j] == "t":
                count += 1
            if S[j] == "t" and j-i >= 2:
                res = max((count-2)/((j-i+1)-2), res)

print(res)