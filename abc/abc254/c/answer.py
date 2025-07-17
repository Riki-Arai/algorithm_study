N, K = map(int, input().split())
A_list = list(map(int, input().split()))

res_list = [None] * N
for i in range(K):
    res_list[i::K] = sorted(A_list[i::K])

A_list.sort()
if res_list == A_list:
    print("Yes")
else:
    print("No")