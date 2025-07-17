N, X = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)]

res = 0
for i, a_list in enumerate(A_lists, 1):
    v, p = a_list
    res += v * p
    if res > X * 100:
        print(i)
        exit()

print(-1)