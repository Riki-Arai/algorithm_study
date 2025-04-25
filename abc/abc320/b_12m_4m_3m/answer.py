S = input().strip()

res = 0
for i in range(len(S)):
    for j in range(len(S)):
        if i + j + 1 <= len(S) and S[i:i+j+1] == S[i:i+j+1][::-1]:
            res = max(res, len(S[i:i+j+1]))

print(res)