N = int(input())
p_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))

res_list = [0] * N
for i in range(N):
    res_list[q_list[i]-1] = q_list[p_list[i]-1]

print(*res_list)
