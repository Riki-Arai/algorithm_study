H, M = list(map(int,input().split()))

while True:
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