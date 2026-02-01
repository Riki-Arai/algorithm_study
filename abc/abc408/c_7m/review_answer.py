N, M = map(int, input().split()) # 取得例：1 2

imos_list = [0]*(N+2)
for _ in range(M):
    L, R = map(int, input().split()) # 取得例：1 2
    imos_list[L] += 1
    imos_list[R+1] -= 1

cum_list = [0]
# 両両は番兵なので除外しておく
for x in imos_list[1:-1]:
    cum_list.append(cum_list[-1]+x)

# 左端は番兵なので除外してminを導出
print(min(cum_list[1:]))