S = input().strip() # 取得例：A
T = input().strip() # 取得例：A

res = 0
for i in range(len(S)):
    if S[i] != T[i]:
        res += 1

print(res)