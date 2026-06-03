N, K = map(int, input().split())
A_list = list(map(int, input().split()))

A_list.sort()

res = A_list[-1] - A_list[0]

max_A = A_list[-1]

B = []
for a in A_list:
    if a == max_A:
        B.append(a)
    else:
        a += ((max_A - a) // K) * K
        B.append(a)

B.sort()
res = min(res, B[-1] - B[0])
for i in range(N - 1):
    now_min = B[i + 1]
    now_max = B[i] + K
    tmp_res = min(now_max-now_min, now_max-B[0])
    res = min(res, now_max - now_min)

print(res)