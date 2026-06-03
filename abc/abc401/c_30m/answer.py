N, K = map(int, input().split()) # 取得例：1 2

if N < K:
    print(1)
else:
    res_list = [1]*K
    res = K