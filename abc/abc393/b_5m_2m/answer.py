S = input().strip()

res = 0
N = len(S)
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i < j < k and abs(j-i) == abs(k-j) and S[i] == "A" and S[j] == "B" and S[k] == "C":
                res += 1

print(res)