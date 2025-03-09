H, W = list(map(int, input().split()))
R, C = list(map(int, input().split()))

res = 0
for i in range(1, H+1):
    h_diff = abs(i - R)
    for j in range(1, W+1):
        w_diff = abs(j - C)
        if h_diff + w_diff == 1:
            res += 1

print(res)
