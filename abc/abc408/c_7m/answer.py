N, M = map(int, input().split()) # 取得例：1 2

imos_list = [0]*(N+2)
for _ in range(M):
    L, R = map(int, input().split())
    imos_list[L] += 1
    imos_list[R+1] -= 1

cum_list = [0]*(N+2)
for i in range(1, len(cum_list)):
    cum_list[i] += imos_list[i]+cum_list[i-1]

1