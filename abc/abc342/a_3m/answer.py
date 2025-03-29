import collections

S_list = list(input().strip())

c_list = collections.Counter(S_list)
for x in c_list:
    if c_list[x] == 1:
        print(S_list.index(x)+1)