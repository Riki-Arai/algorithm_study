N, M = list(map(int, input().split()))
A_list = list(map(int, input().split()))

res_list = []
for n in range(1, N+1):
    if n not in A_list:
        res_list.append(n)

print(len(res_list))
res_list.sort()
res_list = list(map(str, res_list))
print(" ".join(res_list))
