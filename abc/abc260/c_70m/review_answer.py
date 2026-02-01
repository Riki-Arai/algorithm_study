N, X, Y = map(int, input().split())

r_dp_list = [0]*11
b_dp_list = [0]*11

b_dp_list[2] = Y
r_dp_list[2] = X*b_dp_list[2]
for i in range(3, N+1):
    b_dp_list[i] = r_dp_list[i-1]+Y*b_dp_list[i-1]
    r_dp_list[i] = r_dp_list[i-1]+X*b_dp_list[i]

print(r_dp_list[N])