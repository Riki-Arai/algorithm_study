N, M, K = map(int, input().split()) # 取得例：1 2

res_list = []
res_set = set()
a_list = [[False]*M for _ in range(N)]
for _ in range(K):
    A, B = map(int, input().split()) # 取得例：1 2
    a_list[A-1][B-1] = True
    if all(a_list[A-1]) and A not in res_set:
        res_list.append(A)
        res_set.add(A)

print(*res_list)