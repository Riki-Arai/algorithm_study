from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

# cnt[d][r] = 桁数が d で、M で割った余りが r の要素数
cnt = defaultdict(int)

for a in A:
    d = len(str(a))
    cnt[(d, a % M)] += 1

ans = 0

for a in A:
    # a の後ろに b を連結する
    # a * 10^d + b
    for d in range(1, 11):
        p = pow(10, d, M)
        target = (-a * p) % M

        # 桁数 d、余り target の b の個数
        ans += cnt[(d, target)]

print(ans)