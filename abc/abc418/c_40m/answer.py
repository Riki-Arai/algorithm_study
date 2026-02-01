import bisect

N, Q = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

A_list.sort()
cum_list = [0]
for a in A_list:
    cum_list.append(cum_list[-1]+a)

for _ in range(Q):
    B = int(input().strip())
    B -= 1
    b_i = bisect.bisect_right(A_list, B)
    if b_i == N:
        print(-1)
    else:
        print(B*(N-b_i)+cum_list[b_i]+1)