import bisect as bi

N, Q = map(int, input().split())
R_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

R_list.sort()
cum_list = [0]
for r in R_list:
    cum_list.append(cum_list[-1]+r)

for _ in range(Q):
    q = int(input())
    print(bi.bisect_right(cum_list, q)-1)