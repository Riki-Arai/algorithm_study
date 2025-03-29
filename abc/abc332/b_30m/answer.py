K, G, M = map(int, input().split())

g, m = 0, 0
for _ in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        if m > g:
            w_1 = m - g
            w_2 = G - g
            if w_1 >= w_2:
                g += w_2
                m -= w_2
            else:
                g += w_1
                m -= w_1
        else:
            w_1 = g - m
            w_2 = M - m
            if w_1 >= w_2:
                g += w_2
                m -= w_2
            else:
                g += w_1
                m -= w_1

print(g, m)