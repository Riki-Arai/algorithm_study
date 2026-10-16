N, M = map(int, input().split()) # 取得例：1 2

c2s_list = [-1]*(M+1)
for _ in range(N):
    C, S = map(int, input().split()) # 取得例：1 2
    c2s_list[C] = max(c2s_list[C], S)

print(*c2s_list[1:])