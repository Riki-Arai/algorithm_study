N = int(input())
P_list = list(map(int, input().split()))

res_list = [0]*N
for i, p in enumerate(P_list):
    l_i = (p-1)%N
    base_i = (l_i-i)%N
    for j in range(3):
        res_list[(base_i+j)%N] += 1

print(max(res_list))