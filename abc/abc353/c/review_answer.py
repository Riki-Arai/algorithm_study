import bisect

n = int(input().strip())
a = list(map(int, input().split()))
# 今回の問題は順番は関係ないので二分探索や尺取法を使えるようにするためにソート
a.sort()

cnt = 0
res = 0

# a[i] + a[j] >= 10^8を満たす組み合わせの個数を二分探索でカウント
for i in range(n):
    # 二分探索でa[i] + a[pos] >= 10^8となる最小のposを探す
    # j>iであるため第3引数にi+1としなければいけない
    pos = bisect.bisect_left(a, 100000000 - a[i], i + 1)
    if pos < n:
        cnt += (n - pos)

# (N-1) * ΣA_i を計算
for i in range(n):
    res += a[i] * (n - 1)

res -= cnt * 100000000

print(res)