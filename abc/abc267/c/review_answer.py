N, M = map(int, input().split())
A_list = list(map(int, input().split()))

res = 0
for i, a in enumerate(A_list[:M], 1):
    res += i*a

cum_list = [0]
for a in A_list:
    cum_list.append(cum_list[-1]+a)

tmp_res = res
for i in range(M, N):
    add_a = A_list[i]
    tmp_res = tmp_res + add_a*M - (cum_list[i]-cum_list[i-M])
    res = max(tmp_res, res)

print(res)