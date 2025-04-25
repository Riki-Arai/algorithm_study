A, B, C, D = map(int, input().split())

ans = -1
diff = C*D-B
if 0 < diff:
    ans = (A+diff-1)//diff
print(ans)


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