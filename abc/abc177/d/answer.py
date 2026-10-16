from atcoder.dsu import DSU


N, M = map(int, input().split()) # 取得例：1 2

dsu = DSU(N)
for _ in range(M):
    A, B = map(int, input().split()) # 取得例：1 2
    dsu.merge(A-1, B-1)

print(max(map(len, list(dsu.groups()))))