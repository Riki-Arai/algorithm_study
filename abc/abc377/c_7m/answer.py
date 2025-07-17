n,m = map(int,input().split())
s = set()
for _ in range(m):
    a,b = map(int,input().split())
    s.add((a,b))
    for i in [-1,1]:
        for j in [-2,2]:
            s.add((a+i,b+j))
            s.add((a+j,b+i))
ans = n*n
for i,j in s:
    if 1<=i<=n and 1<=j<=n:
        ans-=1
print(ans)