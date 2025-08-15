W, H, x, y = map(int, input().split()) # 取得例：1 2

a1 = H/W
a2 = H/-W
if a1*x == y or a2*x + H == y:
    if (a1*x == a2*x + H):
        print(W*H/2, 1)
    exit()

if x == 0 or x == W:
    res1 = min(W*y, W*abs(H-y))
    res2 = H*W/2 * (max(y, H-y)/H)
    if res1 == res2:
        print(res1, 1)
    else:
        print(max(res1, res2), 0)
    exit()
elif y == 0 or y == H:
    res1 = min(x*H, abs(W-x)*H)
    res2 = H*W/2 * (max(x, W-x)/W)
    if res1 == res2:
        print(res1, 1)
    else:
        print(max(res1, res2), 0)
    exit()


res1 = min(W*y, W*abs(H-y))
res2 = min(x*H, abs(W-x)*H)
print(max(res1, res2), 0)