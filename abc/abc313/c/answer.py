N = int(input())
A_list = list(map(int, input().split()))

sum_v = sum(A_list)
ave_v = sum_v//N
if sum_v % 2 == 0:
    n_list = [ave_v] * N
else:
    n_list = [ave_v] * N + [ave_v+1]

res = 0
A_list.sort()
for i, a in enumerate(A_list):
    res += abs(n_list[i]-a)


if sum_v % 2 == 0:
    print(res//2-1)
else:
    print(res//2)