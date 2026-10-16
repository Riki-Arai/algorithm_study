'''
(1) 愚直な方法だとさすがにTLE
(2) 1桁ずつ減ることに着目し、そこから累積和を思いつく
(3) 1の位から順番に決めていくと整合性は取れそうだが、そこでも普通の数字で扱うとTLEになってしまった
(4) そこでそれぞれの位でリストに格納するようにした
(5) 整数系の問題はたまに筆算で扱うものがあったりするのでこの着想も持っておくと良さそう
'''
import sys; sys.setrecursionlimit(10**7)

X = input().strip()

cum_list = [0]
for x in X:
    cum_list.append(cum_list[-1]+int(x))

res_list = []
m = 0
k = 1
for i in range(len(cum_list)-1, -1, -1):
    new_m, r = divmod(cum_list[i]+m, 10)
    res_list.append(str(r))
    m = new_m

print(int("".join(reversed(res_list))))