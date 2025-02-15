import sys
import itertools

list_ = list(sys.stdin)
for input_ in list_:
    n, x = list(map(int, input_.split()))
    if n == 0 and x == 0: 
        break
    count = 0
    list_ = range(1, n+1)
    c_list = list(itertools.combinations(list_, 3))
    for c in c_list:
        if c[0] + c[1] + c[2] == int(x):
            count += 1

    print(count)
