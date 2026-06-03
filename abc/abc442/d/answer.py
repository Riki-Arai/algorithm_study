N, Q = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

cum_list = [0]
for a in A_list:
    cum_list.append(cum_list[-1]+a)

for _ in range(Q):
    q = list(map(int, input().split())) # 取得例：1 2
    if q[0] == 1:
        _, x = q
        cum_list[x] += A_list[x]-A_list[x-1]
        cum_list[x+1] = A_list[x-1]+cum_list[x]
        A_list[x-1], A_list[x] = A_list[x], A_list[x-1]
    else:
        _, l, r = q
        print(cum_list[r]-cum_list[l-1])