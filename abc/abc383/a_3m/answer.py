N = int(input())

res, count = 0, 0
for _ in range(N):
    T, V = list(map(int, input().split()))
    if count == 0:
        post_T = T
    else:
        res -= (T - post_T)
        post_T = T
        if res < 0:
            res = 0
    res += V
    count += 1

print(res)
