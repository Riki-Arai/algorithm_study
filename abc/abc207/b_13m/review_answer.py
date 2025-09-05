A, B, C, D = map(int, input().split())

if C*D <= B:
    print(-1)
else:
    res = 0
    while A+B*res > D*C*res:
        res += 1
    print(res)


### first
#A, B, C, D = map(int, input().split())
#
#if C*D > B:
#    res = 0
#    r_num = 0
#    while r_num * D < A:
#        A += B
#        r_num += C
#        res += 1
#    print(res)
#
#else:
#    print(-1)