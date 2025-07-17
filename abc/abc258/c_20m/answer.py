N, Q = map(int, input().split()) # 取得例：1 2
S = input().strip() # 取得例："A"

sl = 0
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        sl = (sl+x) % len(S)
    else:
        print(S[(x-1-sl)])