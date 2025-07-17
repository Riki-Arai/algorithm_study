N = int(input())
S = input().strip()

res = 0
for i in range(N-2):
    if S[i] == "#" and S[i+1] == "." and S[i+2] == "#":
        res += 1

print(res)