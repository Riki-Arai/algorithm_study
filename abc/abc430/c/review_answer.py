import bisect as bi

N, A, B = map(int, input().split())
S = input()

a_cum_list = [0]
b_cum_list = [0]
for s in S:
    if s == "a":
        a_cum_list.append(a_cum_list[-1]+1)
        b_cum_list.append(b_cum_list[-1])
    else:
        a_cum_list.append(a_cum_list[-1])
        b_cum_list.append(b_cum_list[-1]+1)

res = 0
for i in range(len(a_cum_list)):
    a_i = bi.bisect_left(a_cum_list, A+a_cum_list[i])
    b_i = bi.bisect_left(b_cum_list, B+b_cum_list[i])-1
    if b_i >= a_i:
        res += b_i-a_i+1

print(res)