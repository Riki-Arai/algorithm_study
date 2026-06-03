import itertools as it

N = int(input())

xy_lists = []
for _ in range(N):
    x, y = map(int, input().split())
    xy_lists.append((x, y))

xy_sets = set(xy_lists)
res = 0
for i, j in it.combinations(xy_lists, 2):
    x, y = i
    xx, yy = j
    if x != xx and y != yy and (xx, y) in xy_sets and (x, yy) in xy_sets:
        res += 1

print(res//2)


from itertools import combinations

n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

S = set(data)
ans = 0
# combinationrの中には対角線に当たる2点も含む
for (x1, y1), (x2, y2) in combinations(data, 2):
    # 直線の関係にあたる点の組み合わせを排除し、対角線の組み合わせだけを残すようにする
    if x1 == x2 or y1 == y2:
        continue
    # 残りの2点で以下の条件を満たしていれば長方形である
    if (x1, y2) in S and (x2, y1) in S:
        ans += 1

# 対角線の選び方は2通りなので最後に2で割る
ans //= 2
print(ans)
