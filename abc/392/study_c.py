n,*p=map(int,open(0).read().split());r=[0]*n
for i in range(n):
    r[p[i+n]-1]=p[p[i]+n-1]
print(*r)
