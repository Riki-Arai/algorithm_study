N, Q = map(int, input().split()) # 取得例：1 2

INF = 10**7+1
x2b_list = [0]*INF
b2n_list = [0]*INF
add_x = 0
for _ in range(Q):
    q, x = map(int, input().split()) # 取得例：1 2
    if q == 1:
        x2b_list[x] += 1
        b2n_list[x2b_list[x]] += 1
        if b2n_list[x2b_list[x]] == N:
            add_x += 1
    else:
        print(b2n_list[x+add_x])