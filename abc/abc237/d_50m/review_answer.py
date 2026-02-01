from collections import deque

n, s = input().split()
n = int(n)

a = deque([n])
for i in range(n - 1, 0 - 1, -1):
    if s[i] == 'L':
        a.append(i)
    else:
        a.appendleft(i)

print(" ".join(map(str, a)))


#N = int(input())
#S = input().strip()
#
#res_list = []
#r_list, l_list = [], []
#for i, s in enumerate(list(S), 1):
#    if i == 1 and s == "R":
#        l_list.append(0)
#        res_list.append(1)
#    elif i == 1 and s == "L":
#        r_list.append(0)
#        res_list.append(1)
#    elif i > 1 and s == "R":
#        pre_s = S[i-2]
#        if pre_s == "L":
#            l_list.append(res_list.pop())
#            r_list.extend(res_list)
#            res_list = [i]
#        else:
#            res_list.append(i)
#    elif i > 1 and s == "L":
#        pre_s = S[i-2]
#        if pre_s == "R":
#            r_list.append(res_list.pop())
#            l_list.extend(res_list)
#            res_list = [i]
#        else:
#            res_list.append(i)
#
#
#if len(S) > 1 and s == "R" and pre_s == "R":
#    print(*l_list+res_list+r_list[::-1])
#else:
#    print(*l_list+res_list[::-1]+r_list[::-1])