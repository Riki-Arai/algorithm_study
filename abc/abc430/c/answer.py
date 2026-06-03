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