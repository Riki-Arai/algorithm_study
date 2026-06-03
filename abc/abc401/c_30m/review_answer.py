N, K = map(int, input().split()) # 取得例：1 2

if N < K:
    print(1)
else:
    res_list = [1]*K
    res = K
    i = 0
    for _ in range(N-K):
        res_list.append(res)
        res += (res_list[-1]%(10**9) - res_list[i]%(10**9))
        i += 1

    print(res%(10**9))