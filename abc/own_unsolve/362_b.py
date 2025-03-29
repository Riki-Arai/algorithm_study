import itertools
import math

A_lists = [list(map(int, input().split())) for _ in range(3)] # 取得例:[[1,2], [3,4]・・[9,10]]

dis_pos = {}
for i in range(3):
    dis_pos[i] = A_lists[i]

l = [0, 1, 2]
comb = itertools.combinations(l, 2)
dis_list = []
for c in comb:
    a = dis_pos[c[0]]
    b = dis_pos[c[1]]
    #dis = math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))
    dis = pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)
    dis_list.append(dis)

max_dis = max(dis_list)
dis_list.remove(max_dis)
#if pow(max_dis, 2) == sum(map(lambda x: x*x, dis_list)):
if max_dis == sum(dis_list):
    print("Yes")
else:
    print("No")