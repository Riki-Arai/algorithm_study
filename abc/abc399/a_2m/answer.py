N = int(input()) # 数値：1
S = input().strip()
T = input().strip()

res = 0
for i in range(N):
    if S[i] != T[i]:
        res += 1

print(res)