import bisect

N = int(input().strip())
v = []
for _ in range(N):
    a, b = map(int, input().split())
    v.append((a, b))

v.sort(key=lambda x: x[0])
lefts = [x[0] for x in v]
res = 0
for i in range(N):
    # -1を行うことで自身のカウントを排除
    j = bisect.bisect_right(lefts, v[i][1]) - 1
    # 意外とこれが大事で、v[i][0]よりも左側の領域を除外するような役役割持つ
    res += j - i

print(res)