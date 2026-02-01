T = int(input())

res_list = []
for _ in range(T):
    N, W = map(int, input().split())
    C_list = list(map(int, input().split()))

    M = 2 * W
    imos_list = [0] * (M + 1)
    for i in range(1, N + 1):
        c = C_list[i - 1]
        L = (-i) % M
        R = (L + W - 1) % M

        if L <= R:
            imos_list[L] += c
            imos_list[R + 1] -= c
        else:
            imos_list[L] += c
            imos_list[M] -= c
            imos_list[0] += c
            imos_list[R + 1] -= c

    cur = 0
    res = 10**30
    for x in range(M):
        cur += imos_list[x]
        res = min(res, cur)

    res_list.append(res)

for res in res_list:
    print(res)