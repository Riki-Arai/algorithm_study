S = input().strip() # 取得例："A"

res = 0
for i in range(len(S)//2):
    if S[i] != S[-1-i]:
        res += 1

print(res)