n = int(input())
a = list(map(int, input().split()))

# 成人の数
s = 0
# i年後に配れなくなる大人の数
r = [0] * n
for i in range(n):
    a[i] += s
    num = min(a[i], n - i - 1)
    # 最終的な値に更新
    a[i] -= num

    s += 1
    # 配れる石がなくなる大人の数をカウント
    r[i + num] += 1

    s -= r[i]

print(*a)