N = int(input())
S = list(input())

res = 0
for i, s in enumerate(S):
    if "." == s:
        if i + 1 < N and i - 1 >= 0:  
            if S[i-1] == "#" and S[i+1] == "#":
                res += 1

print(res)
