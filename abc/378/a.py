import collections

a_list = list(map(int, input().split()))
c_list = collections.Counter(a_list)
res = 0
for v in c_list.values():
    res += v // 2
print(res)
