N, S = map(int, input().split())
A_list = list(map(int, input().split()))

cum_list = [0]
for i in range(2*N):
    cum_list.append(cum_list[-1]+A_list[i%N])

S %= sum(A_list)
c_set = set(cum_list)
for c in cum_list:
    if c+S in c_set:
        print("Yes")
        break

else:
    print("No")