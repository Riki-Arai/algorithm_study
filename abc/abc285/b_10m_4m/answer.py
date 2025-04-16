N = int(input())
S = input().strip()

for i in range(N-1):
    res = 0
    for l in range(N-i):
        for k in range(l):
            if S[k] != S[k+i+1]:
                continue
            else:
                break
        else:
            res = max(res, l)

    print(res)