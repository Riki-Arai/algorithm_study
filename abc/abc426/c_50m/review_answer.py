# Nの数が大きくない点と古いバージョンを管理しなくて良い点に着目できた
N, Q = map(int, input().split())

v_list = [1]*(N+1)
v_list[0] = 0
under_x = 1
for _ in range(Q):
    X, Y = map(int, input().split())
    res = 0
    if X >= under_x:
        for x in range(under_x, X+1):
            n = v_list[x]
            res += n
            v_list[Y] += n
            v_list[x] = 0
        under_x = X
        print(res)
    else:
        print(res)