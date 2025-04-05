N = int(input())
S = input().strip()

res = S[0]
for i in range(1, N):
    if S[i-1]+S[i] == "na":
        res += "ya"
    else:
        res += S[i]
print(res)