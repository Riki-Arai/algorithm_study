A, B, C, D = map(int, input().split())
res = int(A/(C*D - B)+1)
if res > 0:
    print(res)
else:
    print(-1)