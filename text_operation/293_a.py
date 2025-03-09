S = input()

res = ""
for i in range(0, len(S) - 1, 2):
    res += S[i+1]
    res += S[i]

print(res)
