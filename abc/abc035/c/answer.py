N, Q = map(int, input().split()) # 取得例：1 2

imos_list = [0]*(N+1)
for _ in range(Q):
    l, r = map(int, input().split()) # 取得例：1 2
    imos_list[l-1] ^= 1
    imos_list[r] ^= 1

res_list = []
tmp_res = 0
for v in imos_list[:-1]:
    tmp_res ^= v
    res_list.append(str(tmp_res))

print("".join(res_list))