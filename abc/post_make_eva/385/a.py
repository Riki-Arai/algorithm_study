import itertools

list_ = list(map(int, input().split()))

c_list = itertools.combinations(list_, 2)

s = set(list_)
res_flag = False
for c in c_list:
    hoge = s - set(c)
    if sum(list(hoge)) == sum(c):
        res_flag = True
        break

if list_.count(list_[0]) == len(list_):
    res_flag = True

if res_flag:
    print("Yes")
else:
    print("No")
