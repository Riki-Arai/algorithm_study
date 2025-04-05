S = input().strip()

N = len(S)
im = 0
res = 0
while im <= N:
    for i in range(N):
        sub_S = S[i:i+im]
        if sub_S == sub_S[::-1]:
            res = max(res, len(sub_S))
    im += 1

print(res)