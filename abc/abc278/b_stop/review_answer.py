# 時計の表示では1文字ずつ見ると0~9で1周であることがポイント
# HとMについても周期性があるので注意(A問題でも似たような出題がある)
H, M = list(map(int,input().split()))

while True:
    # A, B, C, Dが0~9で1周なのでdivmodでは10を使う
    h0,h1 = divmod(H,10)
    m0,m1 = divmod(M,10)
    x = h0*10+m0
    y = h1*10+m1
    if 0 <= x < 24 and 0 <= y < 60:
        print(H,M)
        exit()
    M += 1
    if M == 60:
        M = 0
        H += 1
        if H == 24:
            H = 0