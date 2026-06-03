import bisect as bi

N, M = map(int, input().split()) # 取得例：1 2
A_list = sorted(map(int, input().split()))
B_list = sorted(map(int, input().split()))

res = 0
b_i = 0
for b in B_list:
    b_i = bi.bisect_left(A_list, b, b_i)
    if b_i == N:
        print(-1)
        exit()
    res += A_list[b_i]
    b_i += 1

print(res)