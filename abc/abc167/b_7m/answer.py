A, B, C, K = map(int, input().split()) # 取得例：1 2

n_list = [A, B, C]
res = 0
v = 1
for i in n_list:
    if K - i > 0:
        res += v * i
        K -= i
    else:
        res += v * K
        print(res)
        break

    v -= 1