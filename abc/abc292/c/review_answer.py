N = int(input())

# num[v] := 「v を x*y として表せる組 (x,y) の個数」
# 1 <= x, y かつ x*y = v の組の数
num = [0] * (N+1)
# 下記は調和級数の性質から O(N log N)である
for x in range(1, N+1):
    limit = N // x  # x*y <= N となる y の最大値
    for y in range(1, limit+1):
        num[x*y] += 1

res = 0
# X+Y=NはN通りしかないのでrange(1, N+1)で探索
for v in range(1, N+1):
    # ABが2パターン、CDが3パターンあれば6パターンあることになるので、それをresに足していく
    # AB=vとしたときにCDはN-vと表すことができる
    res += num[v] * num[N - v]

print(res)