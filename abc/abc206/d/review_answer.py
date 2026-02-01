from atcoder.dsu import DSU

N = int(input())
A = list(map(int, input().split()))

uf = DSU(max(A)+1)
for i in range(N//2):
    uf.merge(A[i], A[N - 1 - i])

ans = 0
for g in uf.groups():
    ans += len(g) - 1

print(ans)