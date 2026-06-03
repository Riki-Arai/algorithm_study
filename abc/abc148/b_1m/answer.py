N = int(input()) # 数値：1
S, T = input().split() # 取得例："A" "B"

res = ""
for i in range(N):
    res += S[i]
    res += T[i]

print(res)