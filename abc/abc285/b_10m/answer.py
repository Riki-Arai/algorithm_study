N = int(input())
S = input().strip()

res = 0
for i in range(1, N):
    for l in range(N-i, -1, -1):
        for k in range(l):
            if S[k] == S[k+i]:
                break
        else:
            print(l)
            break
    res = 0