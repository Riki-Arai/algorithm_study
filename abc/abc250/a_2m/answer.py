H, W = map(int, input().split())
R, C = map(int, input().split())

res = 0
for i in range(H):
    for j in range(W):
        if abs(i - (R-1)) + abs(j - (C-1)) == 1:
            res += 1
print(res)