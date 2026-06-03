import bisect as bi

N = int(input().strip())
A_list = list(map(int, input().split()))

A_list.sort()
cum_list = [0]
for a in A_list:
    cum_list.append(cum_list[-1]+a)

MOD = 10**8
res = 0
count = 0
for i, a in enumerate(A_list, 1):
    b_i = bi.bisect_left(A_list, MOD-a, i)
    res += ((N-i)*a + cum_list[len(cum_list)-1]-cum_list[i])
    count += N-b_i

print(res-MOD*count)