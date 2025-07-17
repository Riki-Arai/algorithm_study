n, m, t = map(int, input().split())
last_time = 0
cur = n
res = True
cafes = [tuple(map(int, input().split())) for _ in range(m)]
cafes.append((t, t))
for a, b in cafes:
    cur -= a - last_time
    if cur <= 0:
        res = False
    # 充電の容量が決まっているのでminを使用
    cur = min(n, cur + (b - a))
    last_time = b
print("Yes" if res else "No")


## first
#N, M, T = map(int, input().split()) # 取得例：1 2
#A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]
#
#res = N
#b_list = [0]
#for A_list in A_lists:
#    a, b = A_list
#    res -= a - b_list[-1]
#    if res <= 0:
#        print("No")
#        exit()
#    res = min(N, res + ((b-a) + 0.5) // 1)
#    b_list.append(b)
#
#if res - (T - b_list[-1]) > 0:
#    print("Yes")
#else:
#    print("No")