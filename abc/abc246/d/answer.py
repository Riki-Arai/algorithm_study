N = int(input())

if N == 0:
    print(0)
    exit()

res = float("INF")
for a in range(1, 10**6+1):
    for b in range((10**6)//(a*a)+1):
        tmp_res = pow(a+b, 3) - 2*(a**2*b) - 2*(a*b**2)
        if tmp_res >= N:
            res = min(tmp_res, res)

print(res)