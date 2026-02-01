T = int(input()) # 数値：1

for _ in range(T):
    na, nb, nc = map(int, input().split()) # 取得例：1 2
    min_v = min(na, nc)
    if min_v > nb:
        na -= nb
        nc -= nb
        max_v = max(na, nc)
        min_v = min(na, nc)
        m, r = divmod(max_v, 2)
        if m >= min_v:
            print(nb+min_v)
        elif m < min_v and r == 1:
            if min_v-m >= 2:
                print(nb+m+1)
            else:
                print(nb+m)
        else:
            print(nb+m)
    else:
        print(min_v)