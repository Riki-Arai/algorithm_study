import bisect as bi

N, M, D = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

B_list.sort()
res = -1
for a in A_list:
    b_i = bi.bisect_right(B_list, a + D)
    if b_i != 0:
        b = B_list[b_i - 1]
        if abs(a - b) <= D:
            res = max(res, a + b)

print(res)