N = int(input())
S = input()

# 1 の位置
p = []

for i in range(N):
    if S[i] == '1':
        p.append(i)

k = len(p)
mid = k // 2
center = p[mid]
ans = 0
# 左側を詰める
# 本来あるべき位置:
# center-1, center-2, ...
for i in range(mid):
    target = center - (mid - i)
    ans += abs(p[i] - target)

# 右側を詰める
# 本来あるべき位置:
# center+1, center+2, ...
for i in range(mid + 1, k):
    target = center + (i - mid)
    ans += abs(p[i] - target)

print(ans)