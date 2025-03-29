import sys

A_list = []
for i in sys.stdin:
    A_list.append(i)

A_list.reverse()
for a in A_list: 
    print(a.rstrip())